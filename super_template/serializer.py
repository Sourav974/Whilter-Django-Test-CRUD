from dataclasses import fields
from rest_framework import serializers
from template.serializers import *
from .models import *


# class BackgroundScoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BackgroundScore
#         fields = '__all__'


class ComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Components
        fields = '__all__'


# class TextElementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TextElement
#         fields = '__all__'


# class LogosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Logos
#         fields = '__all__'


# class OverlaysSerializer(serializers.ModelSerializer):
#     text_element = TextElementSerializer(many=True)
#     logos = LogosSerializer(many=True)

#     class Meta:
#         model = Overlays
#         fields = ['text_element', 'logos']


class SuperTemplateSerializer(serializers.ModelSerializer):
    background_score = BackgroundScoreSerializer()
    components = ComponentsSerializer(many=True)
    overlays = OverlaysSerializer()

    class Meta:
        model = SuperTemplate
        fields = ['business', 'types', 'duration',
                  'template_url', 'background_score', 'components', 'overlays']


class CreateSuperTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperTemplate
        fields = '__all__'
