from django.shortcuts import render, HttpResponse,redirect

from app0.models import Department,UserInfo,FileInfo
# Create your views here.


def index(request):
    return render(request, 'index.html')


def tpl(request):

    name = "韩超"
    role = ['CEO','管理员','文件保管']
    user_info = {"name":"test_one", "salary": 100000, "role": "CTO"}

    data_list = [
        {"name": "test_one", "salary": 100000, "role": "CTO"},
        {"name": "test_2", "salary": 100000, "role": "CEO"},
        {"name": "test_3", "salary": 100000, "role": "CPO"},
        {"name": "test_4", "salary": 100000, "role": "CMO"}
    ]
    return render(request, 'tpl.html', {"n1": name, "n2": role, "n3": user_info, "n4": user_info})


def  news(req):
    import requests
    #
    res = requests.get("http://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=3&r=0.8968549847944927&callback=jQuery111207955381438833715_1691560595066&_=1691560595069")
    if res.status_code != 200:
        print("Error({})".format(res.status_code))
    else:
        print(res.content)
       # data_lists = res.json()
       # print(data_lists)
        import json
        # texts = res.content
        # json_data = texts[46:]
        # ret = json.loads(json_data)
        # print(json_data)

    return render(req, 'news.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    #
    obj = UserInfo.objects.filter(email=name, pwd=pwd).first()
    if obj == None:
        return render(request, 'login.html', {'error_msg':"用户名或密码错误"})
    #
    return redirect("/index")


def info_list(request):
    data_list = UserInfo.objects.all()
    return render(request, 'info_list.html', {"items":data_list})


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


#
def user_list(request):
    objs = UserInfo.objects.all()
    for obj in objs:
     print(obj.department_id, obj.get_gender_display(), obj.create_time.strftime('%Y-%m-%d'))
    return render(request, "user_list.html", {"users" : objs})


def user_add(request):
    if request.method == 'GET':
        depart = Department.objects.all().order_by('id')
        print(depart)
        return render(request, 'user_add.html', {"departs" : depart})

    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    #
    ret = UserInfo.objects.create(name=name, email=email, phone=phone, pwd=pwd)
    print(ret)
    return redirect("/user/list")


def user_edit(request, nid):
    if request.method == 'GET':
        obj = UserInfo.objects.filter(id=nid).first()
        print(nid ,obj)
        depart = Department.objects.all().order_by('id')
        return render(request, "user_edit.html", {"obj" : obj, "departs":depart})
    #
    id = request.POST.get('id')

    UserInfo.objects.update(id=id)

    return HttpResponse("编辑成功")


def file_list(request):

    files = FileInfo.objects.all().order_by('create_time')
    return render(request, "file_list.html", {"files": files})

################################################################
from django import models

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['id', 'name', 'email', 'phone']


def user_model_form_add(request):
    form = UserModelForm()
    return render(request, 'model_form_add.html', {"form":form})

