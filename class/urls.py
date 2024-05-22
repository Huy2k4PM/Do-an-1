from django.contrib import admin
from django.urls import path
from . import views
# from .views import LoginClass

urlpatterns = [
    path('home',views.home_views,name='home'),
    path('logout',views.logout_views,name = 'logout'),
    path('signup',views.signup_views,name = 'signup'),
    path('login/',views.login_views, name = 'login'),
    path('search',views.search_views,name = 'search'),
    path('product/',views.product_views,name = 'product'),
    path('',views.product_list, name='product_list'),
    path('shoping_cart/',views.shopping_cart_views,name = 'shopping_cart'),
    path('OrderDetail/',views.Order_view,name = 'oderdetail'),
    path('get_user_cart/',views.get_user_cart,name = 'get_user_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('feedback/',views.feedback,name="feedback")
]
