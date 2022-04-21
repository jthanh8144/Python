from rest_framework import serializers
from django.contrib.auth.models import User
from . models import *


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(
        max_length=None, min_length=None, allow_blank=True)
    firstname = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=6)
    re_password = serializers.CharField(max_length=255, min_length=6)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'password')


class ChangePassSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, min_length=6)
    new_password = serializers.CharField(max_length=255, min_length=6)
    rnew_password = serializers.CharField(max_length=255, min_length=6)


class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=None, min_length=None, allow_blank=True)
    firstname = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    img = serializers.ImageField(allow_null=True)
    default_address = serializers.CharField(
        max_length=None, min_length=None, allow_null=True)
    ship_address = serializers.CharField(
        max_length=None, min_length=None, allow_null=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('title', 'name', 'email', 'phone', 'content')


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class UpdateCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    operator = serializers.CharField(max_length=1)


class CheckoutSerializer(serializers.Serializer):
    address = serializers.CharField(
        max_length=None, min_length=None, allow_null=True, required=False)


class OrderAdminSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()


class ProductAdminSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class UpdateProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
