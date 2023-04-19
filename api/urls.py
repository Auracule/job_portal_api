from django.urls import path, include
# from unicodedata import lookup
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('category',views.CategoryViewSet, basename='category')
router.register('listjobs', views.ListjobViewSet, basename='listjobs')
router.register('employee', views.EmployeeViewSet, basename= 'employee')
router.register('employer', views.EmployerViewSet, basename= 'employer')
router.register('contact', views.ContactViewSet, basename='contact')
router.register('application', views.ApplicationViewSet, basename='application')
router.register('blogcat', views.BlogCatViewSet, basename='blogcat')
router.register('blogpost', views.BlogPostViewSet, basename='blogpost')

comment_router = routers.NestedDefaultRouter(router, 'blogpost', lookup='blogpost')
comment_router.register('comment', views.CommentViewSet, basename= 'blogpost-comment')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(comment_router.urls)),
]



