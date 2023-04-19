from templated_mail.mail import BaseEmailMessage
from django.conf import settings
from .models import *

# django-templated-email
def send_email_contact(full_name, email, subject, message):
    try:
        message = BaseEmailMessage(template_name='api/email_contact.html',
        context = {
            'full_name': full_name,
            'email': email,
            'subject':subject,
            'message':message,
        })
        message.send([email, settings.EMAIL_HOST])
        print('Sent')
    except Exception as e:
        print('Failed' , e)

        
    
def send_email_applicant(full_name, email):
    try:
        employer_email = Employee.objects.get(user__email=email)
        msg = BaseEmailMessage(template_name='api/employee_email.html',
        context = {
            'employer_email': employer_email.application_set.values('jobs__employer__user__email'),
            'full_name': full_name,
            'email': email,
        })
        msg.send([email, employer_email])
        print(f'Employer: {employer.email}')
        print('Received')
        print(f'Employee: {email}')
        print('Sent')
    except Exception as e:
        print('Failed' , e)




































































































































































# employer_email
# def send_employer_email(full_name, employer_email, cv, date_applied):
#     try:
#         employer_email = Employee.objects.get(user__email=email).values('application_set__jobs__employer__user__email')
#         message= BaseEmailMessage(template_name= '/api/employer_email.html',
#         context = {
#             'full_name': full_name,
#             'employer_email': employer_email.application_set__jobs__employer__user__email,
#             'cv':cv,
#             'date_applied':date_applied,
#         })
#         message.send([email, employer_email])
#         print('employer sent')
#     except Exception:
#         print('failed to send')