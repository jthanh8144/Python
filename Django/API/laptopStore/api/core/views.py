import re
import requests
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *
from rest_framework_simplejwt import *
from .serializers import *
from .models import *
from drf_yasg.utils import swagger_auto_schema

# User


def validpassword(p):
    if len(p) < 6 or not re.search("[a-z]", p) or not re.search("[0-9]", p):
        return False
    return True


@swagger_auto_schema(methods=['POST'], request_body=RegisterSerializer,
                     responses={200: "{'status': 'register success'}",
                                404: "{'status': 'You must enter all fields'}"
                                + "\n{'status': 'User alrealdy exist'}"
                                + "\n{'status': 'Password contains at least 6 characters. It must contain letters and numbers.'}"
                                + "\n{'status': 'Password not match'}"})
@api_view(['POST'])
def register(request):
    user = request.data
    username = user['username']
    email = user['email']
    firstname = user['firstname']
    lastname = user['lastname']
    password = user['password']
    rpassword = user['re_password']
    if username == '' or email == '' or password == '' or rpassword == '':
        return Response({'status': 'You must enter all fields'})
    if User.objects.filter(username=username).exists():
        return Response({'status': 'User alrealdy exist'})
    elif User.objects.filter(email=email).exists():
        return Response({'status': 'Email alrealdy exist'})
    elif validpassword(password) == False:
        return Response({'status': 'Password contains at least 6 characters. It must contain letters and numbers.'})
    elif rpassword != password:
        return Response({'status': 'Password not match'})
    else:
        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        Cart.objects.create(user=user)
        Profile.objects.create(user=user)
        return Response({'status': 'register success'})


@swagger_auto_schema(methods=['POST'], request_body=LoginSerializer,
                     responses={200: "{'access': token,\n'refresh': token,\n'username': username,\n'status': 'Login success'}",
                                404: "{'detail': 'Incorrect authentication credentials.'}"})
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not User.objects.filter(username=username).exists() or User.objects.filter(email=username).exists():
        raise exceptions.AuthenticationFailed()
    if User.objects.filter(email=username).exists():
        username = User.objects.get(email=username).username
    user = authenticate(username=username, password=password)
    if user is None:
        raise exceptions.AuthenticationFailed()
    token_endpoint = reverse(viewname='token_obtain_pair', request=request)
    token = requests.post(token_endpoint, data=request.data).json()
    response = Response()
    response.data = {
        'access': token.get('access'),
        'refresh': token.get('refresh'),
        'username': username,
        'status': 'Login success'
    }
    return response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    return Response()


@swagger_auto_schema(methods=['PUT'], request_body=ChangePassSerializer,
                     responses={200: "{'status': 'success'}",
                                404: "{'status': 'Incorrect Password'}"
                                + "\n{'status': 'New Password not match'}"
                                + "\n{'status': 'Password not strong enough'}"})
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changePassword(request):
    username = request.user
    new_password = request.data.get('new_password')
    rnew_password = request.data.get('rnew_password')
    user = User.objects.get(username=username)
    if user.check_password(request.data.get('password')) == False:
        return Response({'status': 'Incorrect Password'})
    else:
        if not new_password == rnew_password:
            return Response({'status': 'New Password not match'})
        elif not validpassword(new_password):
            return Response({'status': 'Password not strong enough'})
    user.set_password(new_password)
    user.save()
    return Response({'status': 'success'})


@swagger_auto_schema(methods=['PUT'], request_body=UpdateUserSerializer,
                     responses={200: "{'status': 'success'}"})
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request):
    username = request.user
    user = request.data
    User.objects.filter(username=username).update(
        email=user['email'], first_name=user['first_name'], last_name=user['last_name'])
    userid = User.objects.get(username=username).id
    if user['default_address'] != '':
        Profile.objects.filter(user_id=userid).update(
            default_address=user['default_address'])
    if user['ship_address'] != '':
        Profile.objects.filter(user_id=userid).update(
            default_address=user['ship_address'])
    if type(user['img']) == type(''):
        Profile.objects.filter(user_id=userid).update(img=user['img'])
    return Response({'status': 'success'})


@swagger_auto_schema(methods=['GET'], request_body=None,
                     responses={200: "Information of user profile."})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user(request):
    username = request.user
    userid = User.objects.get(username=username).id
    queryset = User.objects.filter(username=username)
    serializers = UserSerializer(queryset, many=True)
    user = serializers.data[0]
    querycart = CartDetail.objects.filter(user_id=userid)
    numProduct = len(CartDetailSerializer(querycart, many=True).data)
    user["num"] = numProduct
    queryset = Cart.objects.filter(user_id=userid)
    cart = CartSerializer(queryset, many=True).data[0]
    user["cart"] = cart
    queryimg = Profile.objects.filter(user_id=userid)
    try:
        profile = ProfileSerializer(queryimg, many=True, context={
                                    'request': request}).data[0]
    except:
        Profile.objects.create(user=serializers.data[0])
        profile = ProfileSerializer(queryimg, many=True, context={
                                    'request': request}).data[0]
    user["img"] = profile['img']
    response = Response()
    response.data = {
        'user': user
    }
    return response


@swagger_auto_schema(methods=['GET'], request_body=None,
                     responses={200: "Information of user profile."})
@swagger_auto_schema(methods=['POST'], request_body=OrderAdminSerializer,
                     responses={200: "{'status': 'Your order has been successfully canceled'}"})
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def userOrder(request):
    if request.method == 'GET':
        username = request.user
        userid = User.objects.get(username=username).id
        queryset = Order.objects.filter(
            user_id=userid).order_by('-created_at')
        orders = OrderSerializer(queryset, many=True).data
        print(orders)
        if len(orders) < 1:
            return Response({'status': "You don't have orders."})
        else:
            for order in orders:
                queryset = OrderDetail.objects.filter(
                    id=order['id'])
                details = OrderDetailSerializer(queryset, many=True, context={
                    'request': request}).data
                order['details'] = details
            return Response(orders)
    else:
        orderid = request.data.get('order_id')
        Order.objects.filter(id=orderid).update(status='canceled')
        return Response({'status': 'Your order has been successfully canceled'})


# products


@swagger_auto_schema(methods=['GET'], request_body=None, responses={200: "List of products"})
@api_view(['GET'])
def products(request):
    queryset = Product.objects.all()
    serializers = ProductSerializer(queryset, many=True, context={
                                    'request': request}).data
    return Response(serializers)


@swagger_auto_schema(methods=['GET'], request_body=None, responses={200: "List of new products"})
@api_view(['GET'])
def newProducts(request):
    queryset = Product.objects.all().order_by('-created_at')[:8]
    serializers = ProductSerializer(queryset, many=True, context={
                                    'request': request}).data
    return Response(serializers)


@swagger_auto_schema(methods=['GET'], request_body=None, responses={200: "List of instock products"})
@api_view(['GET'])
def instockProducts(request):
    queryset = Product.objects.all().order_by('-stock')[:8]
    serializers = ProductSerializer(queryset, many=True, context={
                                    'request': request}).data
    return Response(serializers)


@swagger_auto_schema(methods=['GET'], request_body=None, responses={200: "List of hot products"})
@api_view(['GET'])
def hotProducts(request):
    queryset = Product.objects.exclude(stock=0).order_by('stock')[:8]
    serializers = ProductSerializer(queryset, many=True, context={
                                    'request': request}).data
    return Response(serializers)


@swagger_auto_schema(methods=['POST'], request_body=SearchSerializer,
                     responses={200: "List of products have name like query.",
                                404: "{'status': 'failed'}"})
@api_view(['POST'])
def searchProducts(request):
    filterdata = "%" + request.data.get('name') + "%"
    try:
        queryset = Product.objects.raw(
            'SELECT * FROM core_product WHERE name LIKE %s', [filterdata])
        serializers = ProductSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializers.data)
    except:
        return Response({'status': 'failed'})


@swagger_auto_schema(methods=['GET'], request_body=None, responses={200: "Detail of product by code"})
@api_view(['GET'])
def detailProduct(request, code):
    queryset = Product.objects.filter(product_code=code)
    serializers = ProductSerializer(queryset, many=True, context={
                                    'request': request}).data[0]
    return Response(serializers)


# brand


@swagger_auto_schema(methods=['GET'], request_body=None, responses={200: "List of brand"})
@api_view(['GET'])
def brand(request):
    queryset = Brand.objects.all()
    serializers = BrandSerializer(queryset, many=True, context={
                                  'request': request}).data
    return Response(serializers)


# feedback


@swagger_auto_schema(methods=['POST'], request_body=FeedbackSerializer,
                     responses={200: "{'status': 'Your feedback has been noted. Staff will be in touch shortly to respond.'}",
                                404: "{'status': 'An error occurred while sending data. please try again later'}"})
@api_view(['POST'])
def sendFeedback(request):
    feedback = request.data.get('feedback')
    print(feedback)
    try:
        Feedback.objects.create(title=feedback['title'], name=feedback['name'],
                                email=feedback['email'], phone=feedback['phone'], content=feedback['content'])
    except:
        return Response({'status': 'An error occurred while sending data. please try again later'})
    return Response({'status': 'Your feedback has been noted. Staff will be in touch shortly to respond.'})


@swagger_auto_schema(methods=['GET'], request_body=None, responses={200: "List of feedback"})
@api_view(['GET'])
@permission_classes([IsAdminUser])
def feedback(request):
    queryset = Feedback.objects.all().order_by('-id')
    serializers = FeedbackSerializer(queryset, many=True)
    return Response(serializers.data)


# cart


@swagger_auto_schema(methods=['GET'], request_body=None, responses={200: "List of products in cart"})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart(request):
    username = request.user
    userid = User.objects.get(username=username).id
    queryset = CartDetail.objects.filter(user_id=userid)
    serializer = CartDetailSerializer(queryset, many=True)
    return Response(serializer.data)


@swagger_auto_schema(methods=['POST'], request_body=AddToCartSerializer,
                     responses={200: "{'status': 'Add to cart success.'}",
                                400: "{'status': 'This product is out of stock.'}"})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addToCart(request):
    username = request.user
    userid = User.objects.get(username=username).id
    productId = request.data.get('product_id')
    if Product.objects.get(id=productId).stock < 1:
        return Response({'status': 'This product is out of stock.'})
    queryset = Product.objects.filter(id=productId)
    serializers = ProductSerializer(queryset, many=True, context={
                                    'request': request}).data[0]
    price = float(serializers['price'])
    haveInCart = CartDetail.objects.filter(
        product_id=productId, user_id=userid)
    serializers = CartDetailSerializer(haveInCart, many=True).data
    cart = Cart.objects.get(user_id=userid)
    if len(serializers) < 1:
        CartDetail.objects.create(
            quantity=1, product_id=productId, user_id=userid)
        Cart.objects.filter(user_id=userid).update(num=cart.num+1)
    else:
        newQuantity = CartDetail.objects.get(
            product_id=productId, user_id=userid).quantity + 1
        CartDetail.objects.filter(
            product_id=productId, user_id=userid).update(quantity=newQuantity)
    cartTotal = cart.total + price
    Cart.objects.filter(user_id=userid).update(total=cartTotal)
    return Response({'status': 'Add to cart success.'})


@swagger_auto_schema(methods=['PUT'], request_body=UpdateCartSerializer,
                     responses={200: "{'status': 'success'}"})
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCart(request):
    username = request.user
    userid = User.objects.get(username=username).id
    productId = request.data.get('product_id')
    operator = request.data.get('operator')
    if operator == 'x':
        CartDetail.objects.filter(
            product_id=productId, user_id=userid).delete()
    else:
        product = Product.objects.get(id=productId)
        stock = product.stock
        # price = product.price
        quantity = CartDetail.objects.get(
            product_id=productId, user_id=userid).quantity
        if operator == '+' and quantity < stock:
            CartDetail.objects.filter(
                product_id=productId, user_id=userid).update(quantity=quantity+1)
        if operator == '-' and quantity > 1:
            CartDetail.objects.filter(
                product_id=productId, user_id=userid).update(quantity=quantity-1)
    queryset = CartDetail.objects.filter(user_id=userid)
    items = CartDetailSerializer(queryset, many=True).data
    print(len(items))
    sum = 0
    for item in items:
        sum += Product.objects.get(id=item['product']
                                   ).price * int(item['quantity'])
    Cart.objects.filter(user_id=userid).update(total=sum, num=len(items))
    return Response({'status': 'success'})


@swagger_auto_schema(methods=['POST'], request_body=CheckoutSerializer,
                     responses={200: "{'status': 'pending'}",
                                400: "{'status': 'Order don't have address'}"})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    username = request.user
    userid = User.objects.get(username=username).id
    profile = Profile.objects.get(user_id=userid)
    address = request.data.get('address')
    if not address:
        if profile.default_address:
            address = profile.default_address
    if not address:
        return Response({'status': "Order don't have address"})
    total = Cart.objects.get(user_id=userid).total
    order = Order.objects.create(
        address=address, total=total, status='pending', user_id=userid)
    queryset = CartDetail.objects.filter(user_id=userid)
    items = CartDetailSerializer(queryset, many=True).data
    for item in items:
        OrderDetail.objects.create(
            quantity=item['quantity'], order_id=order.id, product_id=item['product'])
        product = Product.objects.get(id=item['product'])
        Product.objects.filter(id=item['product']).update(
            stock=(product.stock - item['quantity']))
    CartDetail.objects.filter(user_id=userid).delete()
    Cart.objects.filter(user_id=userid).update(total=0, num=0)
    return Response({'status': 'pending'})


# admin


@swagger_auto_schema(methods=['GET'], request_body=None,
                     responses={200: "List of orders"})
@swagger_auto_schema(methods=['POST'], request_body=OrderAdminSerializer,
                     responses={200: "{'status': 'Change status success'}"})
@swagger_auto_schema(methods=['DELETE'], request_body=OrderAdminSerializer,
                     responses={200: "{'status': 'Cancel order success'}"})
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAdminUser])
def orderAdmin(request):
    if request.method == 'GET':
        queryset = Order.objects.all().order_by('-created_at')
        orders = OrderSerializer(queryset, many=True).data
        for order in orders:
            orderid = order['id']
            user = User.objects.get(id=order['user'])
            name = user.first_name + ' ' + user.last_name
            order['fullname'] = name
            queryset = OrderDetail.objects.filter(order_id=orderid)
            details = OrderDetailSerializer(queryset, many=True, context={
                                            'request': request}).data
            order['details'] = details
        return Response(orders)
    elif request.method == 'POST':
        orderid = request.data.get('order_id')
        order = Order.objects.get(id=orderid)
        if order.status == 'pending':
            order.status = 'confirmed'
            order.save()
        elif order.status == 'confirmed':
            order.status = 'done'
            order.save()
        return Response({'status': 'Change status success'})
    elif request.method == 'DELETE':
        orderid = request.data.get('order_id')
        Order.objects.filter(id=orderid).update(status='canceled')
        return Response({'status': 'Cancel success'})


@swagger_auto_schema(methods=['DELETE'], request_body=ProductAdminSerializer,
                     responses={200: "{'status': 'Delete prodcut success'}"})
@swagger_auto_schema(methods=['POST'], request_body=ProductSerializer,
                     responses={200: "{'status': 'Add product success'}",
                                404: "{'status': 'Productcode or Productname alrealdy exist'}"})
@swagger_auto_schema(methods=['PUT'], request_body=UpdateProductSerializer,
                     responses={200: "{'status': 'Update prodcut success'}"})
@api_view(['POST', 'DELETE', 'PUT'])
@permission_classes([IsAdminUser])
def productAdmin(request):
    if request.method == 'DELETE':
        productid = request.data.get('product_id')
        Product.objects.filter(id=productid).delete()
        return Response({'status': 'Delete product success'})
    else:
        productcode = request.data.get('product_code')
        brandid = request.data.get('brand_id')
        name = request.data.get('name')
        price = request.data.get('price')
        img = request.data.get('img')
        description = request.data.get('description')
        stock = request.data.get('stock')
        brand = Brand.objects.get(id=brandid)
        if request.method == 'POST':
            if (Product.objects.filter(product_code=productcode).exists()) == False and (Product.objects.filter(name=name).exists()) == False:
                Product.objects.create(product_code=productcode, name=name, price=price,
                                       description=description, img=img, brand_id=brandid, stock=stock)
                return Response({'status': 'Add product success'})
            else:
                return Response({'status': 'Productcode or Productname alrealdy exist'})
        if request.method == 'PUT':
            productid = request.data.get('id')
            Product.objects.filter(id=productid).delete()
            Product.objects.create(id=productid, product_code=productcode, brand_id=brand.id,
                                   name=name, price=price, img=img, description=description, stock=stock)
            return Response({'status': 'Update product success'})
