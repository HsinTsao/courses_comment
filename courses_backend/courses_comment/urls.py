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
    path('admin/', admin.site.urls),
    # path('', include('app_01.urls')),
    url(r'^auth/', include(router.urls)),
    url(r'^test/', app_01.views.TestView.as_view()),
    # path('api/', app_01.views.APIViewSet),
    url(r'docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION,
                                    authentication_classes=[],
                                    permission_classes=[]))
]
