from rest_framework import serializers
from website.models import *
from django.contrib.auth.models import User, Group
from django_filters import rest_framework as filters
from rest_framework.serializers import SerializerMethodField

class PostSerializer(serializers.ModelSerializer):
	class Meta:
	    model = Post
	    fields = '__all__'

