import django_filters
from .models import Project, Milestone
  

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['name', 'description','service_provider','status']
        
    def __init__(self,*args, **kwargs):
        super(ProjectFilter, self).__init__(*args, **kwargs)
        self.filters['name'].label = "Type project name to search"
        self.filters['description'].label = "Type project description to search"
        self.filters['service_provider'].label = "Filter by service provider"
        self.filters['status'].label = "Filter by project status"