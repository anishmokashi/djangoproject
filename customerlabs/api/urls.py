
from django.urls import include, path
from .views import *
from api.views import CompanyViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)#this will allow all methods get ,put ,post delete on company
router.register(r'employees',EmployeeViewSet)
urlpatterns = [
    path('',include(router.urls))

]
