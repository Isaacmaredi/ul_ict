from django.contrib import admin
from .models import Team, Milestone, Project
# Register your models here.

class MilestoneInline(admin.TabularInline):
    model = Milestone
    extra = 0
    
class TeamInline(admin.TabularInline):
    model = Team
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','start_date','end_date','total_cost',
                    'service_provider','status')
    inlines = [MilestoneInline, TeamInline]
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','project_role','project')
    
@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('name','start_date','planned_end_date',
                    'actual_end_date','status','weight','amount','is_paid')
    
    list_editable = ('start_date','planned_end_date','actual_end_date','status',
                    'weight','amount','is_paid')



  