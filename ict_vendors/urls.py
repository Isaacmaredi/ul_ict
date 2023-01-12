from django.urls import path
from . import views

app_name = 'ict_vendors'


urlpatterns =[
    path('vendor_list/', views.VendorListView.as_view(), name='vendor-list'),
    path('vendor_admin/', views.VendorAdminListView.as_view(), name='vendor-admin'),
    path('vendor_add/',views.VendorCreateView.as_view(), name='vendor-add'),
    path('<int:pk>/update/',views.VendorUpdateView.as_view(), name='vendor-update'),
    path('<int:pk>/detail/',views.VendorDetailView.as_view(), name='vendor-detail'),
    path('<int:pk>/detail_admin/',views.VendorAdminDetailView.as_view(), name='vendor-detail-admin'),
    path('<int:pk>/delete/',views.VendorDeleteView.as_view(), name='vendor-delete'),
]