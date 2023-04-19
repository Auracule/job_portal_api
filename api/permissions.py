from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated, DjangoModelPermissions


class IsEmployeeOrEmployer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)





























































































































        # if request.user.is_authenticated and request.user.user_type == 'employer':
        #     employer = Employer.objects.create().exists()
        # return IsAuthenticated()

# class IsEmployeeOrEmployer(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_authenticated and request.user.user_type == 'employer':
#             return IsAdminUser()
#         return IsAuthenticated()
    
    # def has_permission(self, request, view):
    #     if request.user.is_authenticated and request.user.user_type == 'employee' and request.user.is_staff:
    #         return IsAuthenticated()
    #     return IsAdminUser()
    

# class BlocklistPermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         ip_addr = request.META['REMOTE_ADDR']
#         blocked = Employer.objects.create().exists()
#         return not blocked
    #  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # else: 
        # return request.user.is_authenticated and request.user.user_type == 'employer' and request.user.is_staff



# class IsEmployeeOrEmployer(BasePermission):
#     def has_permission(self, request, view):
#         # Check if user is authenticated
#         if not request.user.is_authenticated:
#             return False
        
#         # Check if user is either an employee or employer
        
#         user_type = request.user.user_type
#         if user.user_type == 'employee':
#             return True
#             elif user_type == 'employer':
#                 return False
#         return user_type in ['employee', 'employer']
