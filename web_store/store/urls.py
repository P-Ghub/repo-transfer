from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('stock_page/<int:storeItem_id>', views.stock_page, name='stock_page'),
    path('confirmation_page/<int:stockItem_id>', views.confirmation_page, name='confirmation_page'),
    path('successful_reg_page/', views.successful_reg_page, name='successful_reg_page'),
    path('successful_order/', views.successful_order, name='successful_order'),
]