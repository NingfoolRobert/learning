"""
用户管理类
"""
from django.shortcuts import render, HttpResponse,redirect
from app0.models import Department,UserInfo,FileInfo
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


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


#
class UserModelForm(forms.ModelForm):
    confirm_pwd = forms.CharField(min_length=6, label="确认密码", widget=forms.PasswordInput)
    phone = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    class Meta:
        model = UserInfo
        fields = ['name', 'pwd', 'confirm_pwd', 'email', 'phone', 'department']
        widgets = {
            #"name": forms.TextInput(attrs={"class": "form-control"}),
            "pwd": forms.PasswordInput,
        }
        #pwd = forms.CharField(attrs={"class": "form-control"}, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            print(name, field)
            # if name == "pwd":
            #     field.widget.attrs = {"class": "form-control", "type": "password"}
            #     continue
            field.widget.attrs = {"class": "form-control"}

    #钩子方法
    def clean_confirm_pwd(self):
        confirm_pwd = self.cleaned_data['confirm_pwd']
        pwd = self.cleaned_data['pwd']

        if confirm_pwd != pwd:
            raise ValidationError("密码不一致")

        return confirm_pwd


def user_model_form_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'model_form_add.html', {"form": form})

    form = UserModelForm(data= request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list")
    return render(request, 'model_form_add.html', {"form": form})


def user_edit(request, nid):
    obj = UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        print(nid ,obj)
        depart = Department.objects.all().order_by('id')
        form = UserModelForm(instance=obj)
        return render(request, "user_edit.html", {"form": form})
    #
    form = UserModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/user/list")
    return render(request, "user_edit.html", {"form": form})


def user_delete(request):
    uid = request.GET.get("uid")
    UserInfo.objects.filter(id=uid).delete()
    return redirect("/user/list")

