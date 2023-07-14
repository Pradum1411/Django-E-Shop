from django.urls import path
from . import views
from .middleware.auth import authmiddleware
urlpatterns = [
    path('', views.home,name='home'),
    path('category/<int:m_id>',views.category,name="category"),
    path('cart/',views.cart,name="cart"),
    path('showcart/',authmiddleware(views.showcart),name="showcart"),
    path('checkout/',authmiddleware(views.checkout),name="checkout"),
    path('order/',views.orderdisplay,name="order"),
  
    path("signup/",views.usersignup,name='signup'),
    path("login/",views.userlogin,name='login'),
    path("logout/",views.userlogout,name='logout')
]
