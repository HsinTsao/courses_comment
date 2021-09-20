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
from rest_framework.decorators import action


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


class CoursesView(viewsets.ModelViewSet):
    # 指定查询集合
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

    # 自定义行为
    # @action(methods=['get'], detail=False, url_name='code')
    # # @action(methods=[指定下面的行为接收什么请求], detail=是不是详情视图如果是不详情视图就是 books/latest)
    # def query(self, request, pk, code):
    #     """
    #     查询某个课程信息
    #     """
    #     print("update_course", code)
    #     # course_obj = Course.objects.get(code=code)
    #     # serializer = self.get_serializer(course_obj)
    #     # return Response(serializer.data)
    #
    #     self.serializer_class = CoursesSerializer
    #     instance = self.get_object(code=code)  # 根据pk得到一个序列化器对象
    #     order_valid = self.get_serializer(instance, request.data)  # 根据数据库对项得到一个序列化器对象
    #     order_valid.is_valid()  # 数据校验
    #     order_valid.save()  # 数据保存
    #     return Response(order_valid.data)  # 返回前端

    # API view 用法
    # def dispatch(self, request, *args, **kwargs):
    #     """
    #     请求到来之后，都要执行dispatch方法，dispatch方法根据请求方式不同触发 get/post/put等方法
    #
    #     注意：APIView中的dispatch方法有好多好多的功能
    #     """
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     courses = Course.objects.all()
    #     serializer_data = CoursesSerializer(courses, many=True)
    #     print(serializer_data.data)
    #     return Response(serializer_data.data)
    #
    # def post(self, request, *args, **kwargs):
    #     """创建一个新的课程"""
    #
    #     # 获取数据
    #     client_data = request.data
    #
    #     # 序列化数据
    #     verified_data = CoursesSerializer(data=client_data)
    #     print(verified_data)
    #
    #     # 校验数据
    #     if verified_data.is_valid():
    #         column = verified_data.save()
    #         # print(verified_data.data) # 需要保存之后才能获取.data
    #         return Response(verified_data.data)
    #     else:
    #         return Response(verified_data.errors, status=400)
    #     # return Response('POST请求，响应内容')
    #
    # def put(self, request, code):
    #     print(request.data)
    #     print(code)
    #     course_obj = Course.objects.get(code=code)
    #     verified_data = CoursesSerializer(instance=course_obj, data=request.data)
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


class StudentsView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
