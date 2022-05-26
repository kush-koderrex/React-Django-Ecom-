from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from email.mime import image
# from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name','description')