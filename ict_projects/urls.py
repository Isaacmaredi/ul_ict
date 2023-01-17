from django.urls import path
from . import views

app_name = 'ict_projects'


urlpatterns =[
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('project_admin/',views.ProjectAdminListView.as_view(), name='project-admin'),
    # path('project_admin/', views.project_list, name='project-admin'),
    path('project_detail/<int:pk>/',views.ProjectDetailView.as_view(), name='project-detail'),
    path('project_add/', views.ProjectCreateView.as_view(), name='project-add'),
    path('project_update/<int:pk>/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('project_admin_detail/<int:pk>/', views.ProjectAdminDetailView.as_view(), name='project-admin-detail'),
    path('project_delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='project-delete'),
]
    