from rest_framework import serializers
from .models import *
# class InflectionTimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= InflectionTime
#         fields= ['data_field']
class ComponentSerializer(serializers.ModelSerializer):
    business = serializers.StringRelatedField(many=True)
    inflection_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = Component
        fields = ['id', 'component_url', 'types', 'sub_type', 'length', 'business', 'inflection_time']
    
class ComponentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields ='__all__'




