from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('jobs/', views.jobs, name='jobs'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('blog/', views.blog, name='blog'),
    path('employer_postdash/', views.employer_postdash, name='employer_postdash'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('post_details/', views.post_details, name='post_details'),
]
