from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('customerclick',views.customerclicked_view,name='customerclick'),
]
