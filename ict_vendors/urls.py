from django.urls import path
from . import views

app_name = 'ict_vendors'


urlpatterns =[
    path('vendors/', views.VendorListView.as_view(), name='vendor-list'),
    path('vendor_admin/', views.VendorAdminListView.as_view(), name='vendor-admin'),
    path('vendor_add/',views.VendorCreateView.as_view(), name='vendor-add'),
    path('vendor_update/<int:pk>/',views.VendorUpdateView.as_view(), name='vendor-update'),
    path('vendor_detail/<int:pk>/',views.VendorDetailView.as_view(), name='vendor-detail'),
    path('vendor_detail_admin/<int:pk>/',views.VendorAdminDetailView.as_view(), name='vendor-detail-admin'),
    path('vendor_delete/<int:pk>/',views.VendorDeleteView.as_view(), name='vendor-delete'),
]