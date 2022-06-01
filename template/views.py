from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class GetTemplate(APIView):
    def get(self, request):
        data = Template.objects.all()
        serializers = TemplateSerializer(data, many=True)
        # print(serializers.data)

        return Response({"status": "success", "data": serializers.data}, status=200)


class CreateTemplate(APIView):
    def post(self, request):

        serializers = CreateTemplateSerializer(data=request.data)
        # print(serializers.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=200)
        else:
            return Response(serializers.errors)


class UpdateTemplate(APIView):
    def put(self, request):
        template = request.GET['template']
        update = Template.objects.get(id=template)
        serializers = CreateTemplateSerializer(
            update, data=request.data, partial=True)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return serializers.errors


class DeleteTemplate(APIView):
    def delete(self, request):
        template = request.GET['template']
        erase = Template.objects.get(id=template)
        erase.delete()
        return Response({'msg':"data deleted"},status=200)


class GetTemplateIdAPI(APIView):
    def get(self, request):
        template = request.GET['template']
        data = Template.objects.get(id=template)
        serializers = TemplateSerializer(data)
        return Response(serializers.data)
