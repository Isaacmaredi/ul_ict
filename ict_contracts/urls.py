from django.urls import path
from . import views

app_name = 'ict_contracts'

urlpatterns = [  
    path('contracts/', views.ContractListView.as_view(), name='contract-list'),
    path('contract_admin/', views.ContractAdminListView.as_view(), name='contract-admin'),
    path('contract_detail/<int:pk>/', views.ContractDetailView.as_view(), name='contract-detail'),
    path('contract_admin_detail/<int:pk>/',views.ContractAdminDetailView.as_view(), name='contract-admin-detail'),
    path('contract_add/', views.ContractCreateView.as_view(), name='contract-add'),
    path('contract_update/<int:pk>/', views.ContractUpdateView.as_view(), name='contract-update'),
    path('contract_delete/<int:pk>/', views.ContractDeleteView.as_view(), name='contract-delete'),
]