from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class GetTemplate(APIView):
    def get(self, request):
        data = Template.objects.all()
        serializers = TemplateSerializer(data, many=True)
        # print(serializers.data)

        return Response({"status": "success", "data": serializers.data}, status=200)
