from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('shopping/', views.shopping, name="shopping"),
    path('payment/', views.payment, name="payment"),
]
