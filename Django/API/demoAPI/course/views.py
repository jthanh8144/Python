from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Course
from . serializers import GetAllCourseSerializer


class GetAllCourseAPIView(APIView):
    def get(self, request):
        list_course = Course.objects.all()
        mydata = GetAllCourseSerializer(list_course, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)
