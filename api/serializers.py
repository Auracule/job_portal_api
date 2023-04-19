from rest_framework import serializers
from rest_framework.serializers import Serializer
from djoser.serializers import UserCreateSerializer as  BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import PasswordResetConfirmSerializer as BasePasswordResetConfirmSerializer
from djoser.serializers import SendEmailResetSerializer as BaseSendEmailResetSerializer
from . models import *
from blog.models import *
from .email import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = ['id', 'title', 'noofjobs']

class ListJobSerializer(serializers.ModelSerializer):
    # employer = serializers.SerializerMethodField()
    class Meta:
        model = ListJobs
        fields = [ 'id','category', 'job_title','company', 'employer', 'location', 'description', 'salary', 'date_posted', 'deadline', 'requirements', 'duty']

    # def get_employer(self, employer: Employer):
    #     return employer.user.value('id')

class UserCreateSerializer(BaseUserCreateSerializer):
    user_type = serializers.ChoiceField(choices=User.USER_TYPE_CHOICES)
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('username','first_name','last_name','email', 'phone', 'profile_img','user_type', 'password')

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('id','username', 'first_name', 'last_name', 'email', 'phone', 'profile_img','user_type')

class EmployeeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    jobs_applied = serializers.SerializerMethodField()
    total_applied = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('id', 'user_id', 'username','first_name', 'email','last_name', 'jobs_applied','total_applied')

    def get_total_applied(self, applicant:Employee):
        return applicant.application_set.count()
    
    def get_jobs_applied(self, obj:Employee):
        return obj.application_set.values('id', 'jobs', 'full_name', 'cv', 'socials', 'date_applied')

class EmployerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    company = serializers.CharField(source='user.first_name')
    email = serializers.EmailField(source='user.email')
    website = serializers.URLField()
    company_address = serializers.CharField(max_length = 255)
    jobs = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    # total_applicants = serializers.SerializerMethodField()
    # jobs = ListJobSerializer(many=True, read_only=True, source='listjobs_set') 

    class Meta:
        model = Employer
        fields = ('id', 'user_id', 'username','company','company_address','website', 'email','jobs','count')
        # fields = ('id', 'user_id', 'username','company','company_address','website', 'email','jobs','count', 'total_applicants')

    def save(self, **kwargs):
        user_id = self.validated_data['user_id']
        full_name = self.validated_data['full_name'],
        employer_email = self.validated_data['email']
        cv = self.validated_data['cv']
        date_applied = self.validated_data['date_applied']
        employer = Employer.objects.create(
            full_name= full_name,
            user_id= user_id,
            cv=cv,
            date_applied=date_applied,
            employer_email=email,
        )
        send_employer_email(full_name, employer_email, cv, date_applied)
        return employer

    def get_jobs(self, obj):
        return obj.listjobs_set.values('id','category__title','job_title')

    def get_count(self, employer: Employer):
        return employer.listjobs_set.count()
    
    def get_total_applicants(self, applicant:Employee):
        return applicant.application_set.count()

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email', 'subject', 'message']

    def save(self, **kwargs):
        full_name = self.validated_data['full_name']
        email = self.validated_data['email']
        subject = self.validated_data['subject']
        message = self.validated_data['message']
        contact = Contact.objects.create(
            full_name = full_name,
            email = email,
            subject = subject,
            message = message
        )
        send_email_contact(full_name, email, subject, message)
        return contact



class ApplicationSerializer(serializers.ModelSerializer):
    jobs_id = serializers.IntegerField()
    class Meta:
        model = Application 
        fields = ['id', 'full_name', 'jobs_id','email','phone', 'role', 'date_applied', 'cv', 'socials']
        
    def save(self, **kwargs):
        full_name = self.validated_data['full_name']
        email = self.validated_data['email']
        jobs_id = self.validated_data['jobs_id']
        phone = self.validated_data['phone']
        cv = self.validated_data['cv']
        socials = self.validated_data['socials']
        application = Application.objects.create(
            full_name = full_name,
            email = email,
            jobs_id = jobs_id,
            phone = phone,
            cv = cv,
            socials = socials
        )
        send_email_applicant(full_name, email)
        return application


class BlogCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCat
        fields = ['id', 'title', 'slug','description']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id' ,'blogcat', 'author', 'title', 'slug','body', 'published', 'pub_date']

class CommentSerializer(serializers.ModelSerializer):
    # blogpost = BlogPostSerializer
    class Meta:
        model = Comment
        fields = ['id', 'user', 'full_name', 'email', 'comment', 'post_created']
































































































































































































    # def update(self, instance, validated_data):
    #     # instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.company_address = validated_data.get('company_address', instance.company_address)
    #     # instance.email =validated_data.get('email', instance.email)
    #     instance.website = validated_data.get('website', instance.website)
    #     instance.save()
    #     return instance 

    # def create(self, validated_data):
    #     return models.Employer.objects.create(**validated_data)






































































        # total_applicants = serializers.SerializerMethodField()
        # fields = ['id', 'full_name','email', 'phone', 'phone', 'role', 'date_applied', 'cv', 'socials']
        # fields = ['id', 'full_name', 'employee', 'jobs','email', 'phone', 'phone', 'role', 'date_applied', 'cv', 'socials', 'total_applicants']

    # def get_total_applicants(self, applicant:Employee):
    #     return applicant.employee_set.count()
        # fields = ['id', 'full_name', 'email', 'phone', 'salary', 'role', 'cv', 'linkedin']




















# class SimpleEmployerSerializer(serializers.ModelSerializer):
#     user_id = serializers.IntegerField(read_only=True)  
#     company = serializers.CharField(source='user.first_name')
#     email = serializers.EmailField(source='user.email')
#     website = serializers.URLField()
#     class Meta:
#         model = Employer
#         fields = ('id', 'user_id','username', 'company', 'company_address', 'website', 'email')

# class EmployerUpdateSerializer(serializers.ModelSerializer):
#     items = SimpleEmployerSerializer(many=True, read_only=True)
#     company_address = serializers.CharField(max_length=225)
#     website = serializers.URLField()
#     class Meta:
#         model = Employer
#         fields = ['id', 'items','company_address', 'website']

#     def update(self, instance, validated_data):
#         # instance.company= validated_data.get('company', instance.company)
#         instance.company_address = validated_data.get('company_address', instance.company_address)
#         instance.email =validated_data.get('email', instance.email)
#         instance.website = validated_data.get('website', instance.website)
#         instance.save()
#         return instance 




  
        
    # def create(self, validated_data):
    #     user_type = validated_data.pop('user_type')
    #     if user_type == 'employer':
    #         Employer.objects.create(user=user)
    #     elif user_type == 'employee':
    #         Employee.objects.create(user=user)
    #     return user







































# class EmployeeCreateSerializer(BaseUserCreateSerializer):
#     username = serializers.CharField(read_only=False, required=True)
#     user_type = serializers.CharField(default='employee', write_only=True)
#     class Meta(BaseUserCreateSerializer.Meta):
#         model = Employee 
#         fields = ['id', 'user_type','username', 'first_name', 'last_name','email', 'phone', 'password']

#         def create(self, validated_data):
#             employee = Employee.objects.create_user(
#                 username=validated_data['username'],
#                 first_name= validated_data['first_name'],
#                 last_name =  validated_data['last_name'],
#                 email = validated_data['email'],
#                 phone= validated_data['phone'],
#                 password= validated_data['password'],
#                 is_employer =False
#             )
#             return employee


# class EmployerCreateSerializer(BaseUserCreateSerializer):
#     user_type = serializers.CharField(default='employer', write_only=True)

#     class Meta(BaseUserCreateSerializer.Meta):
#         model = Employer 
#         fields = ['id' , 'user_type','company', 'company_address', 'website', 'email', 'phone', 'password']

#         def create(self, validated_data):
#             employer = Employer.objects.create_user(
#                 company = validated_data['company'],
#                 company_address = validated_data['company_address'],
#                 website = validated_data['website'],
#                 email = validated_data['email'],
#                 phone = validated_data['phone'],
#                 is_employer = True 
#             )
#             return employer





