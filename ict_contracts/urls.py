from django.urls import path
from . import views

app_name = 'ict_contracts'

urlpatterns = [  
    path('contract_list/', views.ContractListView.as_view(), name='contract-list'),
    path('contract_admin/', views.ContractAdminListView.as_view(), name='contract-admin'),
    path('<int:pk>/contract_detail', views.ContractDetailView.as_view(), name='contract-detail'),
    path('<int:pk>/contract_admin_detail',views.ContractAdminDetailView.as_view(), name='contract-admin-detail'),
    path('contract_add/', views.ContractCreateView.as_view(), name='contract-add'),
    path('<int:pk>/contract_update/', views.ContractUpdateView.as_view(), name='contract-update'),
    path('<int:pk>/contract_delete/', views.ContractDeleteView.as_view(), name='contract-delete'),
]