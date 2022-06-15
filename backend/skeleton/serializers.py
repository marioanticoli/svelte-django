from rest_framework import serializers
from .models import Template, Section


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Template
        fields = ['url', 'name', 'created_at', 'updated_at']


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ['url', 'title', 'template', 'priority', 'content', 'created_at', 'updated_at']


