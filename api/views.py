from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from . filters import *
from . models import *
from blog.models import *
from . permissions  import *
from . serializers import *
from rest_framework.decorators import action

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListjobViewSet(ModelViewSet):
    queryset = ListJobs.objects.all().order_by('id')
    serializer_class = ListJobSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ListjobFilter
    search_fields = ['job_title', 'category__title', 'location']
    permission_classes = [IsEmployeeOrEmployer]

    def create(self, request):
        serializers = ListJobSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(employer = request.user.employer)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    

    
class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user).prefetch_related('application_set')

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsEmployeeOrEmployer()]
        return [IsAdminUser()]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        employee = Employee.objects.get(user__id=request.user.id)
        if request.method == 'GET':
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user).prefetch_related('listjobs_set')

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return EmployerUpdateSerializer
        else:
            return EmployerSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsEmployeeOrEmployer()]
        return [IsAdminUser()]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        employer = Employer.objects.get(user__id=request.user.id)
        if request.method == 'GET':
            serializer = EmployerSerializer(employer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = EmployerSerializer(employer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def  get_queryset(self):
        return super().get_queryset()
    

class BlogCatViewSet(ModelViewSet):
    queryset = BlogCat.objects.all().order_by('id')
    serializer_class = BlogCatSerializer

class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.all().order_by('id')
    serializer_class = BlogPostSerializer

    # def get_serializer_context(self):
    #     return {'blogpost':self.kwargs['blogpost_pk']}

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.filter(blogpost_id = self.kwargs.get('blogpost_pk')).all()
    























































































































































    # def create(self, request):
    #     # listjobs_id = request.data.get('listjobs_id')
    #     # job = ListJobs.objects.get(id=jobs)
    #     serializers = ApplicationSerializer(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save(employee = request.user.employee)
    #         # serializers.save(employee = request.user.employee, listjobs_id=job)
    #         return Response(serializers.data, status= status.HTTP_200_OK)
    #     else:
    #         return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)





































































































# class EmployeeViewSet(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeCreateSerializer


# from djoser.serializers import UserCreateSerializer
# from .models import User

# class UserCreateSerializer(UserCreateSerializer):
#     user_type = serializers.ChoiceField(choices=User.USER_TYPE_CHOICES)

#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('email', 'username', 'password', 'user_type')

# from rest_framework import generics
# from rest_framework.permissions import AllowAny
# # from .serializers import CustomUserCreateSerializer
# from . serializers  import *
# from .models import User

# class EmployerCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = UserCreateSerializer
    

#     def perform_create(self, serializer):
#         serializer.save(user_type=User.UserType.EMPLOYER)

# class EmployeeCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = UserCreateSerializer

#     def perform_create(self, serializer):
#         serializer.save(user_type=User.UserType.EMPLOYEE)
