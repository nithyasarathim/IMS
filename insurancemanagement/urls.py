from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from insurance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('customer/',include('customer.urls')),
]
