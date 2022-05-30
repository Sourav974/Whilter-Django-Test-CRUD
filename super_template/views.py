from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class GetSuperTemplate(APIView):
    def get(self, request):
        data = SuperTemplate.objects.all()
        serializer = SuperTemplateSerializer(data, many=True)

        return Response({"status": "success", "data": serializer.data}, status=200)


class CreateSuperTemplate(APIView):
    def post(self, request):
        serializer = CreateSuperTemplateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors)


class UpdateSuperTemplate(APIView):
    def put(self, request):
        template = request.GET['template']
        update = SuperTemplate.objects.get(id=template)
        serializer = CreateSuperTemplateSerializer(
            update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DeleteSuperTemplate(APIView):
    def delete(self, request):
        template = request.GET['template']
        erase = SuperTemplate.objects.get(id=template)
        erase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetSuperTemplateId(APIView):
    def get(self, request):
        template = request.GET['template']
        data = SuperTemplate.objects.get(id=template)
        serializer = CreateSuperTemplateSerializer(data)
        return Response(serializer.data)
