from django.urls import path
from . import views

app_name = 'ict_projects'


urlpatterns =[
    path('projects_list/', views.ProjectListView.as_view(), name='project-list'),
    path('project_admin/',views.ProjectAdminListView.as_view(), name='project-admin'),
    # path('project_admin/', views.project_list, name='project-admin'),
    path('<int:pk>/project_detail/',views.ProjectDetailView.as_view(), name='project-detail'),
    path('project_add/', views.ProjectCreateView.as_view(), name='project-add'),
    path('<int:pk>/project_update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/project_admin_detail/', views.ProjectAdminDetailView.as_view(), name='project-admin-detail'),
    path('<int:pk>/project_delete', views.ProjectDeleteView.as_view(), name='project-delete'),
]
    