"""
URL configuration for test_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from app0 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index', views.index),
    path('tpl', views.tpl),
    path('news', views.news),
    path('login', views.login),
    path('info/list', views.info_list),

    path('user/add', views.user_add),
    path('user/<int:nid>/edit', views.user_edit),
    path('user/list', views.user_list),
    path('department/add', views.department_add),
    path('department/list', views.department_list),
    path('department/delete', views.department_delete),
    path('department/<int:nid>/edit', views.department_edit),
    path('file/list', views.file_list),
    path('user/model/form/add', views.user_model_form_add),

]
