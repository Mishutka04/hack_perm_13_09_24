
from rest_framework import serializers
from .models import AttrTemplate, Template


class AttrTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttrTemplate
        fields = "__all__"

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"
