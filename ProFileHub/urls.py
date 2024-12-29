"""
URL configuration for ProFileHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from PortfolioApp.views import Home, DownloadCVView, ReferenceView,PostBug, BugReportsView,WebsitePolicyView, Technical_Skills,Introduction,SkillListView, ProjectView, CurrentProjectView, PastProjectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("Home/", Home.as_view(), name="home"),
    path("", Home.as_view(), name='home page'),
    path("intro/", Introduction.as_view(), name="intro"),
    path("Git-Activities/", CurrentProjectView.as_view(), name="current_repo"),  # Corrected path
    path("Repo/", PastProjectView.as_view(), name="past_projects"),  # Corrected path
    path('skill/', Technical_Skills.as_view(), name='technical_skill'),
    path('policies/', WebsitePolicyView.as_view(), name='website_policies'),
    path('reference/', ReferenceView.as_view(), name='reference_list'),
    path('viewe-comment/', BugReportsView.as_view(), name='bug_reports'),
    path('report-bug/', PostBug.as_view(), name='post_comment'),
    path('download-cv/', DownloadCVView.as_view(), name='download_cv'),

]
