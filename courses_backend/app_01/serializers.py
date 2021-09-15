from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'is_staff')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('code', 'name_en', 'url', 'term', 'year')
        extra_kwargs = {
            'code': {
                'required': True,
                'help_text': '课程代号'
            },
            'name_en': {
                'required': True,
                'help_text': '课程英文名称'
            },
            'url': {
                'required': True,
                'help_text': 'handbook链接'
            },
            'term': {
                'required': True,
                'help_text': '学期'
            },
            'year': {
                'required': True,
                'help_text': '学年'
            },

        }
