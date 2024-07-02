from django.urls import path
from . import views

urlpatterns = [
    path('claim_devices.html', views.claim_devices, name='claim_devices_html'),
    path('claim_devices/', views.claim_devices, name='claim_devices'),
    path('success/', views.success_view, name='success'),
    path('delete_device/<str:pk>/', views.delete_device, name='delete_device'),
    path('delete_vlan/<str:pk>/', views.delete_vlan, name='delete_vlan'),
    path('vlan/', views.vlan, name='vlan'),
    path('vlan.html', views.vlan, name='vlan_html'),
    path('delete_wifi/<int:pk>/', views.delete_wifi, name='delete_wifi'),
    path('wifi/', views.wifi, name='wifi'),
    path('wifi.html', views.wifi, name='wifi_html'),
    path('process_csv/', views.process_csv, name='process_csv'),
    path('', views.index, name='index'),
]
