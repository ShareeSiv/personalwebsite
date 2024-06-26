from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('projects/<slug:slug>', views.ProjectDetailView.as_view(), name="project"),
]
