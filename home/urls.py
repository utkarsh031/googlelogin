from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('logout',views.logout_view),
    path('regi',views.regi),
    path('login',views.login),
]