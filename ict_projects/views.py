from django.http import Http404
from django.shortcuts import render, redirect
from django.db.models.aggregates import Count,Sum
from django.db.models import F, Q, Value, DecimalField
from django.db.models.functions import Coalesce
from decimal import Decimal
from django.views.generic import (ListView, DetailView,
                                DeleteView,CreateView, UpdateView,
                                )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .models import *
from .filters  import ProjectFilter


# Create your views here.
class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, *args, **kwargs):
        context = super(FilteredListView,self).get_context_data(*args,**kwargs)

            
        context['filterset'] = self.filterset
        context['form'] = self.filterset.form
    
        context['total_projects'] = self.filterset.qs.count()
        
        return context
    
    

class ProjectListView(LoginRequiredMixin, FilteredListView):
    model = Project
    template_name = 'ict_projects/project_list.html'
    filterset_class = ProjectFilter
    context_object_name = 'projects'
    paginate_by = 8
    
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProjectListView,self).get_context_data(*args, **kwargs)

    #     return context

class ProjectAdminListView(LoginRequiredMixin,FilteredListView):
    model = Project
    template_name = 'ict_projects/project_admin.html'
    filterset_class = ProjectFilter
    context_object_name = 'projects'
    paginate_by = 8
    
        
        
        
        # context['projects'] = Project.objects.annotate(
        #             milestones_count=Count(
        #             'milestones')
        #             ).annotate(
        #             completed_milestones=Count(
        #             'milestones',
        #             filter=(Q(milestones__status__exact='Completed') & Q(milestones__is_paid=True))       
        #             )
        #         ).annotate(
        #             total_progress=Sum(F('milestones__weight'), 
        #             filter=(Q(milestones__status__exact='Completed') & Q(milestones__is_paid=True)) 
        #             )
        #         )

        # return context
    
class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name ='ict_projects/project_update.html'
    
class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project 
    template_name = 'ict_projects/project_detail.html'
    context_object_name = 'project'
    

    def get_context_data(self, queryset=None, *args, **kwargs): 
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
    
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        print('-'*25)
        print('PRIMARY KEY IS: ',pk)
        print('-'*25)
            
        context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
        
        context['total_spent'] = queryset.aggregate(
            total_spent= Coalesce(
                        Sum('milestones__amount', 
                        filter=Q(milestones__is_paid=True) & Q(milestones__status="Completed")
                        ), Value(0, output_field=DecimalField())
                    ) 
                )['total_spent'] 
        
        context["balance"] = self.object.total_cost -  queryset.aggregate(
                                    amount_outstanding= Coalesce(
                                        Sum('milestones__amount', 
                                        filter=Q(milestones__is_paid=True) & Q(milestones__status="Completed")   
                                        ,output_field=DecimalField()), Value(0,output_field=DecimalField())
                                    )
                                )['amount_outstanding']
        
        context['total_progress'] = queryset.aggregate(
                    total_progress= Coalesce(
                        Sum(F('milestones__weight'), 
                        filter=(Q(milestones__status__exact='Completed') & Q(milestones__is_paid=True)),
                        output_field=DecimalField()), 
                        Value(0,output_field=DecimalField())
                    ) 
                )['total_progress']
        return context

    
class ProjectAdminDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'ict_projects/project_admin_detail.html'
    context_object_name = 'project'
    
class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    template_name = 'ict_projects/project_confirm_delete.html'
    success_url = reverse_lazy('ict_projects:project-admin')
    
    
    
    
    
    
    