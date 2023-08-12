from django.shortcuts import render, HttpResponse,redirect

from app0.models import Department
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def department_add(request):

    if request.method == 'GET':
        return render(request,'department_add.html')

    name = request.POST.get('name')
    print(name)
    # if name == None:
    #     return render(request,'department_add.html', {"error":"请输入部门名称"})

    # depart = models.Department.objects.filter(name=name).first()
    # if depart != None:
    #     return render(request,'department_add.html', {"error": "部门已存在"})

    Department.objects.create(name=name)
    return redirect('/department/list')


def department_list(request):
    if request.method == 'GET':
        departs = Department.objects.all().order_by('id')
        print(departs)
        return render(request, 'department_list.html', {"departs": departs})


def department_delete(request):
    nid = request.GET.get('nid')

    obj = Department.objects.filter(id=nid).first()
    print(nid, obj)
    ret = Department.objects.filter(id=nid).delete()
    print(ret)
    return redirect('/department/list')


def department_edit(request, nid):
    if request.method == 'GET':
        print(nid)
        obj = Department.objects.filter(id=nid).first()
        return render(request, 'department_edit.html', {"obj":obj})

    name = request.POST.get('name')
    ret = Department.objects.filter(id=nid).update(name=name)
    if ret == None:
        obj = Department.objects.filter(id=nid).first()
        return render(request, 'department_edit.html', {"obj":obj, "error":"部门名称已存在"})
    return redirect('/department/list')
