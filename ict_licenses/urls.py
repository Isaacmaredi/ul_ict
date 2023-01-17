from django.urls import path

from . import views

app_name = 'ict_licenses'
 
urlpatterns = [  
    path('licenses/', views.LicenseListView.as_view(), name='license-list'),
    path('license_admin/', views.LicenseAdminListView.as_view(), name='license-admin'),
    path('license_detail/<int:pk>/', views.LicenseDetailView.as_view(), name='license-detail'),
    path('license_admin_detail/<int:pk>/',views.LicenseAdminDetailView.as_view(), name='license-admin-detail'),
    path('license_add/', views.LicenseCreateView.as_view(), name='license-add'),
    path('license_update/<int:pk>/', views.LicenseUpdateView.as_view(), name='license-update'),
    path('license_renew/<int:pk>/', views.LicenseRenewView.as_view(), name='license-renew'),
    path('license_delete/<int:pk>/', views.LicenseDeleteView.as_view(), name='license-delete'),
]
