from django.urls import path
from .import views

urlpatterns = [
    path('',views.User,name='user'),
    path('payment',views.PaymentPage,name='payment')
]