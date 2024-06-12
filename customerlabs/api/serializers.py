#create serializers here
#serializers are used to convert json to data and data to json
from rest_framework import serializers

from api.models import company,Employee
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=company
        fields="__all__"#this means i want to include all feilds of company model
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()

    class Meta:
        model=Employee
        fields="__all__"