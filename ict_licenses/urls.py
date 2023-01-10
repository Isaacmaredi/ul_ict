from django.urls import path

from . import views

app_name = 'ict_licenses'
 
urlpatterns = [  
    path('license_list/', views.LicenseListView.as_view(), name='license-list'),
    path('license_admin/', views.LicenseAdminListView.as_view(), name='license-admin'),
    path('<int:pk>/license_detail', views.LicenseDetailView.as_view(), name='license-detail'),
    path('<int:pk>/license_admin_detail',views.LicenseAdminDetailView.as_view(), name='license-admin-detail'),
    path('license_add/', views.LicenseCreateView.as_view(), name='license-add'),
    path('<int:pk>/license_update/', views.LicenseUpdateView.as_view(), name='license-update'),
    path('<int:pk>/license_renew/', views.LicenseRenewView.as_view(), name='license-renew'),
    path('<int:pk>/license_delete/', views.LicenseDeleteView.as_view(), name='license-delete'),
]
