from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('order/<int:pk>/', views.CreateOrderView.as_view(), name='order'),

]
