from dataclasses import fields
from rest_framework import serializers

from lexirus.models import Language
from lexirus.models import InputDocument

# Language Serializer
class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = '__all__'


# Input Document Serializer
class InputDocumentSerilizer(serializers.ModelSerializer):
	class Meta:
		model = InputDocument
		fields = '__all__'
