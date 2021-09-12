from django.shortcuts import render

# Create your views here.

from . import models
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, Group
from app_01.serializers import SubjectSerializer, UserSerializer, GroupSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     允许组查看或编辑的API路径。
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class APIViewSet(viewsets.ModelViewSet):
    # models.Subject.objects.create(code='COMP9444',
    #                               name_en='Neural Networks and Deep Learning',
    #                               url='https://www.handbook.unsw.edu.au/undergraduate/courses/2022/COMP9444/')
    serializer_class = SubjectSerializer


class TestView(APIView):
    def dispatch(self, request, *args, **kwargs):
        """
        请求到来之后，都要执行dispatch方法，dispatch方法根据请求方式不同触发 get/post/put等方法

        注意：APIView中的dispatch方法有好多好多的功能
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')