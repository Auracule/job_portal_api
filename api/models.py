from django.db import models
from django.contrib.auth.models import AbstractUser
from . validators import validate_file_size
from django.core.validators import MinValueValidator, FileExtensionValidator
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    Employee = 'Employee'
    Employer = 'Employer'

    USER_TYPE_CHOICES = [
        (Employee, 'Employee'),
        (Employer, 'Employer'),
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Employee')
    profile_img = models.FileField(upload_to='profile', default='profile.jpg',validators= [
        validate_file_size, FileExtensionValidator(allowed_extensions=['png', 'jpg', 'svg', 'webp'])
    ])
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_address = models.TextField()
    website = models.URLField(null=True, blank=True)
    # company = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField()
    # phone = models.TextField()

    def __str__(self):
        return self.user.username 
        # return self.company.username 
    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField()
    # phone = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    title = models.CharField(max_length=200)
    noofjobs = models.IntegerField()
    description  = models.TextField(default='one', null=True, blank=True)

    def __str__(self):
        return self.title 


class ListJobs(models.Model):
    DUTY = [
        ('Freelance', 'Freelance'),
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time'),
        ('Remote', 'Remote'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, blank=True, null=True)
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField(null=True, blank=True)
    salary = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_now=True)
    requirements = models.TextField()
    duty = models.CharField(max_length=50, choices=DUTY, default= 'Freelance')

    def __str__(self):
        return self.job_title
        
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
class Application(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True) #application_set__employee
    jobs = models.ForeignKey(ListJobs, on_delete=models.CASCADE, null=True) #application_set__listjob
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    # salary = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_applied = models.DateTimeField(auto_now_add=True)
    cv = models.FileField(upload_to= 'api/application', default='cv.pdf', validators= [
    validate_file_size, FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg'])])
    socials = models.URLField()
    
    def __str__(self):
        return self.full_name
    
class BlogCat(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()

class BlogPost(models.Model):
    blogcat = models.ForeignKey(BlogCat, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    post_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blogpost.title
    