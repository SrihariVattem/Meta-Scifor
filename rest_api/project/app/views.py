
from rest_framework.decorators import api_view

from .models import Employee
from .seriaizer import EmployeeSerialize
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def get(request):
    employee_obj=Employee.objects.all()
    serialize=EmployeeSerialize(employee_obj,many=True)
    return Response(serialize.data)

@api_view(['POST'])
def add(request):
    serialize=EmployeeSerialize(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)

@api_view(['PUT'])
def put(request,id):
    emp_obj=Employee.objects.get(id=id)
    serialize=EmployeeSerialize(instance=emp_obj,data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)

@api_view(['PATCh'])
def patch(request,id):
    emp_obj=Employee.objects.get(id=id)
    serialize=EmployeeSerialize(instance=emp_obj, data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)

@api_view(['DELETE'])
def delete(request,id):
    emp_obj=Employee.objects.get(id=id)
    emp_obj.delete()
    return Response('Employee is Deleted')