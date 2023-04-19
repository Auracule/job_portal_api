import django_filters
from django_filters.rest_framework import FilterSet 
from . models import *

class ListjobFilter(FilterSet):
    description = django_filters.LookupChoiceFilter(lookup_choices='description')
    
    class Meta:
        model = ListJobs
        fields = {
            'category_id': ['exact'],
        }