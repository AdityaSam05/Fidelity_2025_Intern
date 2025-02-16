from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import StudentSerial
from rest_framework import status
from .models import Student
from rest_framework_swagger.views import get_swagger_view
import pkg_resources

# Create your views here.

@api_view(['GET'])
def getData(request):
    l1=[10,20,30]
    return Response({'l':l1}, status=200)

@api_view(['POST']) # Create a serializer module as we are using POST
def postData(request):
    return Response("Hello rest!")

@api_view(['POST'])
def create_student(request):
    std=StudentSerial(data=request.data)
    if(std.is_valid()):
        std.save()
        return Response("Successfully Created!",status=status.HTTP_201_CREATED)
    return Response(std.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAll(request):
    stud=Student.objects.all()
    serial=StudentSerial(stud,many=True)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getId(request,pk):
    try:
        stud=Student.objects.get(stu_Id=pk)
        serial=StudentSerial(stud)
        return Response(serial.data,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response(serial.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def std_update(request,pk):
    stud=Student.objects.get(stu_Id=pk)
    serial1=StudentSerial(stud,data=request.data)
    if(serial1.is_valid()):
        serial1.save()
        return Response(serial1.data,status=status.HTTP_201_CREATED)
    return Response(serial1.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def std_delete(request,pk):
    try:
        stud=Student.objects.get(stu_Id=pk)
        stud.delete()
        return Response("Deleted Successfully!",status=status.HTTP_201_CREATED)
    except Student.DoesNotExist:
        return Response("Does not exist!",status=status.HTTP_400_BAD_REQUEST)
    

# schema_view=get_swagger_view(title='api-view')
    