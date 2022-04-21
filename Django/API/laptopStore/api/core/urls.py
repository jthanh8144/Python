from django.urls import path
from .views import *

urlpatterns = [
    path('user/', user, name='user'),
    path('user/register/', register, name='register'),
    path('user/login/', login, name='login'),
    path('user/logout/', logout, name='logout'),
    path('user/changepass/', changePassword, name='changePass'),
    path('user/updateuser/', updateUser, name='updateUser'),
    path('user/order/', userOrder, name='userOrder'),
    path('products/', products, name='products'),
    path('products/new/', newProducts, name='newProduct'),
    path('products/search/', searchProducts, name='searchProduct'),
    path('products/instock/', instockProducts, name='instockProduct'),
    path('products/hot/', hotProducts, name='hotProduct'),
    path('products/<str:code>/', detailProduct, name='detailProduct'),
    path('brand/', brand, name='brand'),
    path('feedback/', feedback, name='feedback'),
    path('feedback/send', sendFeedback, name='sendFeedback'),
    path('cart/', cart, name='cart'),
    path('cart/add', addToCart, name='addToCart'),
    path('cart/update', updateCart, name='updateToCart'),
    path('cart/checkout', checkout, name='checkout'),
    path('admin/order', orderAdmin, name='orderAdmin'),
    path('admin/product', productAdmin, name='productAdmin'),
]
