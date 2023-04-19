from . models import Employee,Employer, User
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender=User)
def create_user_choice(sender, created, instance, *args, **kwargs):
    if created:
        if instance.user_type == 'Employee':
            Employee.objects.create(user=instance)
            # Employee.objects.create(username=instance)
            
            instance.save()
        elif instance.user_type == 'Employer':
            Employer.objects.create(user=instance)
            # Employer.objects.create(company=instance)
            instance.is_staff = True
            instance.save()






# @receiver(post_save, sender=User)
# def create_user_choice(sender, created, instance, *args, **kwargs):
#     if created:
#         if instance.user_type == 'Employee':
#             Employee.objects.create(user=instance)
#             # Employee.objects.create(username=instance)
#             instance.save()
#         elif instance.user_type == 'Employer':
#             Employer.objects.create(user=instance)
#             # Employer.objects.create(company=instance)
#             instance.save()








# @receiver(post_save, sender=User)
# def create_employee_for_user(sender, **kwargs):
#     if kwargs['created'].user_type == 'employee':
#         Employee.objects.create(user=kwargs['instance'])

# @receiver(post_save, sender=User)
# def create_employer_for_user(sender, **kwargs):
#     if kwargs['created'].user_type == 'employer':
#         Employer.objects.create(user=kwargs['instance'])