from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from.serializers import cylinderserializer
from.models import cylinder
from cylinderapp.pagination import get_pagination


class CylindeView(APIView):



    def get(self,request):
        cylinde = cylinder.objects.all().order_by('-id')
        cylinders=get_pagination(request,cylinde,2)
        serializer = cylinderserializer(cylinders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




    def post(self,request):
        serializer = cylinderserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


