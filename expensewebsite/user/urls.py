from django.urls import path
from . import views


urlpatterns = [
    path('user_finance', views.user_finance, name='user_finance')
]
