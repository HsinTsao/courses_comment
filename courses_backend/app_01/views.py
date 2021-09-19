from django.shortcuts import render

# Create your views here.

from . import models
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, Group
from app_01.models import Course, Students
from app_01.serializers import CoursesSerializer, UserSerializer, GroupSerializer, StudentsSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json


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

# class APIViewSet(viewsets.ModelViewSet):
#     # models.Subject.objects.create(code='COMP9444',
#     #                               name_en='Neural Networks and Deep Learning',
#     #                               url='https://www.handbook.unsw.edu.au/undergraduate/courses/2022/COMP9444/')
#     serializer_class = SubjectSerializer


class CoursesView(APIView):
    def dispatch(self, request, *args, **kwargs):
        """
        请求到来之后，都要执行dispatch方法，dispatch方法根据请求方式不同触发 get/post/put等方法

        注意：APIView中的dispatch方法有好多好多的功能
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer_data = CoursesSerializer(courses, many=True)
        print(serializer_data.data)
        return Response(serializer_data.data)

    def post(self, request, *args, **kwargs):
        """创建一个新的课程"""

        # 获取数据
        client_data = request.data

        # 序列化数据
        verified_data = CoursesSerializer(data=client_data)
        print(verified_data)

        # 校验数据
        if verified_data.is_valid():
            column = verified_data.save()
            # print(verified_data.data) # 需要保存之后才能获取.data
            return Response(verified_data.data)
        else:
            return Response(verified_data.errors, status=400)
        # return Response('POST请求，响应内容')

    def put(self, request, code):
        print(request.data)
        print(code)
        course_obj = Course.objects.get(code=code)
        verified_data = CoursesSerializer(instance=course_obj, data=request.data)
        # 校验数据
        if verified_data.is_valid():
            column = verified_data.save()
            # print(verified_data.data) # 需要保存之后才能获取.data
            return Response(verified_data.data)
        else:
            return Response(verified_data.errors, status=400)

    # def put(self, request, column_id):
    #     column_obj = Column.objects.get(pk=column_id)
    #     verified_data = ColumnSerializer(instance=column_obj, data=request.data)
    #     # 校验数据
    #     if verified_data.is_valid():
    #         column = verified_data.save()
    #         # print(verified_data.data) # 需要保存之后才能获取.data
    #         return Response(verified_data.data)
    #     else:
    #         return Response(verified_data.errors, status=400)

    # def delete(self, request, column_id):
    #     column_obj = Column.objects.get(pk=column_id)
    #     column_obj.delete()
    #     return Response({'message': 'OK'})


class StudentsView(APIView):
    def dispatch(self, request, *args, **kwargs):
        """
        请求到来之后，都要执行dispatch方法，dispatch方法根据请求方式不同触发 get/post/put等方法

        注意：APIView中的dispatch方法有好多好多的功能
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        students = Students.objects.all()
        serializer_data = StudentsSerializer(students, many=True)
        print(serializer_data.data)
        return Response(serializer_data.data)

    def post(self, request, *args, **kwargs):
        """创建一个新的用户"""

        # 获取数据
        client_data = request.data

        # 序列化数据
        verified_data = StudentsSerializer(data=client_data)
        print(verified_data)

        # 校验数据
        if verified_data.is_valid():
            column = verified_data.save()
            # print(verified_data.data) # 需要保存之后才能获取.data
            return Response(verified_data.data)
        else:
            return Response(verified_data.errors, status=400)
        # return Response('POST请求，响应内容')

    def put(self, request, name):
        print(request.data)
        print(name)
        student_obj = Students.objects.get(name=name)
        verified_data = StudentsSerializer(instance=student_obj, data=request.data)
        # 校验数据
        if verified_data.is_valid():
            column = verified_data.save()
            # print(verified_data.data) # 需要保存之后才能获取.data
            return Response(verified_data.data)
        else:
            return Response(verified_data.errors, status=400)
