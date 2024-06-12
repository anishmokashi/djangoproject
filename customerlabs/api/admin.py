from django.contrib import admin

# Register your models here.

from django.contrib import admin
from api.models import company,Employee
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)
admin.site.register(company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
#to create super user we have to run the command python manage.py createsuperuser and 
#give name email and password which we used to login on http://127.0.0.1:8000/admin