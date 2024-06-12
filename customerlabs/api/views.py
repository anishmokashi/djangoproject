

from requests import Response
from rest_framework import viewsets #this has inbuilt all crud operation methods defined in it
from api.models import company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=CompanySerializer

    #url=companies/{companyid}/employees
   
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
         try:
                company.objects.get(pk=pk)
                emps=Employee.objects.filter(company=company)
                emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
                return Response(emps_serializer.data)
         except Exception as e:
              print(e)
              return Response({
                   'message':'Company might not exist !! Error'
              })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer