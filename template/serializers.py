from dataclasses import fields
from rest_framework import serializers
from .models import *


class BackgroundScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundScore
        fields = '__all__'


class TextElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextElement
        fields = '__all__'


class LogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logos
        fields = '__all__'


class OverlaysSerializer(serializers.ModelSerializer):
    text_element = TextElementSerializer(many=True)
    logos = LogosSerializer(many=True)

    class Meta:
        model = Overlays
        fields = ['text_element', 'logos']


class ComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Components
        fields = '__all__'


class TemplateSerializer(serializers.ModelSerializer):

    background_score = BackgroundScoreSerializer()
    overlays = OverlaysSerializer()
    components = ComponentsSerializer(many=True)

    class Meta:
        model = Template
        fields = ['id', 'business', 'types', 'watermark', 'duration',
                  'template_url', 'background_score', 'components', 'overlays']
