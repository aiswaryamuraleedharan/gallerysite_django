from django.urls import path
from .import views

urlpatterns = [
    path('',views.Productadmin,name='productadmin'),
    path('update/<str:pk>',views.Update,name='update'),
    path('delete/<str:pk>',views.DeleteUser,name='delete')
]