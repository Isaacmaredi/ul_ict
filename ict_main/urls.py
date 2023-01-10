"""ict_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),
    path('', include('ict_accounts.urls'), name='accounts'),
    path('contracts/', include('ict_contracts.urls'), name ='contracts'), 
    path('licenses/', include('ict_licenses.urls'), name ='licenses'), 
    path('profiles/', include('ict_profiles.urls'), name='profiles'), 
    path('projects/', include('ict_projects.urls'), name='projects'), 
    path('vendors/', include('ict_vendors.urls'), name='vendors'),
    path('dashboard/', include('ict_dash.urls'), name='dash'), 
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# admin.site.site_header ='UL ICT Contracts and Portfolio Admin' 
# admin.site.index_title ='Manage ICT Contracts and Portfolio'