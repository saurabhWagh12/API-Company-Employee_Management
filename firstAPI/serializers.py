from rest_framework import serializers
from app.models import *
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'        



