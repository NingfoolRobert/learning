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
from app0.views import user, department, file, index,account,task,order,test

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index', index.index),
    #path('tpl', views.tpl),
    #path('news', views.news),
    path('login', account.login),
    path('logout', account.logout),
    path('img/code', account.img_code),
    #path('info/list', views.info_list),

    path('user/add', user.user_add),
    path('user/<int:nid>/edit', user.user_edit),
    path('user/list', user.user_list),
    path('user/delete', user.user_delete),
    path('department/add', department.department_add),
    path('department/list', department.department_list),
    path('department/delete', department.department_delete),
    path('department/<int:nid>/edit', department.department_edit),
    path('file/list', file.file_list),
    path('file/add', file.file_add),
    path('file/<int:fid>/edit', file.file_edit),
    path('user/model/form/add', user.user_model_form_add),
    path('task/list', task.task_list),
    path('task/ajax', task.task_ajax),


    #订单管理
    path('order/list', order.order_list),
    path('order/add', order.order_add),
    path('order/edit', order.order_edit),
    path('order/delete', order.order_delete),

    #test
    path('test/md5', test.test_md5),

]
