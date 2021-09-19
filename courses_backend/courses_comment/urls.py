"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls import url
import app_01.views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
API_TITLE = 'courses comment api documentation'
API_DESCRIPTION = 'courses comment api server for courses comment'


router = routers.DefaultRouter()
router.register(r'users', app_01.views.UserViewSet)
# router.register(r'groups', app_01.views.GroupViewSet)

urlpatterns = [
    # 管理员页面
    path('admin/', admin.site.urls),
    url(r'^auth/', include(router.urls)),

    # 课程接口
    # url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),
    # url(r'^test/', app_01.views.TestView.as_view()),
    # 利用正则组起别名 提取url路径参数 关键字参数,
    # #如果给正则组起了别名,那么对应的形参名必须和别名一致
    url(r'^courses/(?P<code>[A-Z]+\d{4})/$', app_01.views.CoursesView.as_view()),

    url(r'^students/(?P<name>.+)/$', app_01.views.StudentsView.as_view()),


    # API文档
    url(r'docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION,
                                    authentication_classes=[],
                                    permission_classes=[]))
]
