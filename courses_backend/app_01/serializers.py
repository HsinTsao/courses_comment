from rest_framework import serializers
from .models import Course, Students
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups', 'is_staff')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'code', 'name_en', 'url', 'term', 'year')
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
                'required': False,
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


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = (
            'id',
            "name",
            "email",
            "password",
            "register_time"
        )

        extra_kwargs = {

        }
