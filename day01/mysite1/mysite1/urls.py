"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('page/1', views.page_1_view),
    path('page/2', views.page_2_view),
    path('page/2003', views.page_2003_view),
    path('page/<int:pg>', views.pagen_view),
    re_path(r'^(?P<v1>\d{1,2})/(?P<op>\w+)/(?P<v2>\d{1,2})$', views.cal2_view),
    path('<int:v1>/<str:op>/<int:v2>', views.cal_view),
    re_path(r'^birthday/(?P<year>\d{4})/(?P<month>[1-9]|1[0-2])/(?P<day>[1-9]|[12][0-9]|3[01])$', views.birthday_view),
    re_path(r'^birthday/(?P<month>[1-9]|1[0-2])/(?P<day>[1-9]|[12][0-9]|3[01])/(?P<year>\d{4})$', views.birthday_view),
]
