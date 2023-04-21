from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import *
from serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail = True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            comp = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=comp)
            emps_serialiser = EmployeeSerializer(emps,many=True,context = {'request':request})
            return Response(emps_serialiser.data)
        
        except: return HttpResponse('<h1 style="text-align:center;">Does Not Exists</h1>')
        

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
