from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/details/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('item/', views.item, name='dashboard-item'),
    path('item/delete/<int:pk>/', views.item_delete, name='dashboard-item-delete'),
    path('item/update/<int:pk>/', views.item_update, name='dashboard-item-update'),
    path('report/', views.report, name='dashboard-report')
]