from django.urls import path, include
from . import views

app_name = 'user_auth'
urlpatterns = [
    #path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('create_user/', views.create_user, name='create_user'),
    path('store_login/', views.store_login, name='store_login'),
]