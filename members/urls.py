from django.urls import path
from . import views

from django.contrib import admin

#from school import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
#initial
    path('login_user',views.login_user,name="login"),
   # end initial
   path('adminlogin',views.adminlogin,name="adminlogin"),

   
   path('adminclick_view',views.adminclick_view,name="adminclick_view"),
    
    path('admin_signup_view',views.admin_signup_view,name="admin_signup_view"),
   
    
 
   
]

   
