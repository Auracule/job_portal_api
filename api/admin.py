from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import *

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", 'user_type',"password1", "password2","first_name", "last_name"),
            },
        ),
    )

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_names', 'last_names', 'email', 'phone']

    @admin.display(description='First Name')
    def first_names(self, employee: Employee):
        return employee.user.first_name

    @admin.display(description= 'Last Name')
    def last_names(self, employee:Employee):
        return employee.user.last_name

    def email(self, employee:Employee):
        return employee.user.email
    
    def phone(self, employee:Employee):
        return employee.user.phone

admin.site.register(Employee, EmployeeAdmin)


class EmployerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'company_address', 'company', 'email', 'phone','website']

    @admin.display(description= 'Company Name')
    def company(self, employer: Employer):
        return employer.user.first_name

    def email(self, employer: Employer):
        return employer.user.email 
    
    def phone(self, employer: Employer):
        return employer.user.phone 

admin.site.register(Employer, EmployerAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display =['id', 'full_name', 'email','subject', 'message']
admin.site.register(Contact, ContactAdmin)

class ListJobsAdmin(admin.ModelAdmin):
    list_display =[ 'id','category','job_title', 'employer','company', 'location', 'description', 'salary', 'date_posted', 'deadline', 'requirements', 'duty']
admin.site.register(ListJobs, ListJobsAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','employee', 'email', 'phone','phone', 'role', 'date_applied', 'cv', 'socials']
admin.site.register(Application, ApplicationAdmin)