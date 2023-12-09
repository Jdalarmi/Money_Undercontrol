from django.urls import path
from . import views


urlpatterns = [
    path('user_finance', views.user_finance, name='user_finance'),
    path('register_user_finance', views.register_user_finance, name='register-user-finance'),
    path('logout_user_finance', views.logout_user_finance, name='logout-user-finance')
]
