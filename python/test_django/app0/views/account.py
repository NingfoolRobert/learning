from django.shortcuts import render, HttpResponse,redirect

from app0.models import Department
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app0.utils.bootstrap import BootStrapForm
from app0.utils.encrypt import md5
from app0.models import UserInfo
from io import BytesIO
from app0.utils.checkcodeimge import check_code


#
class UserLoginForm(BootStrapForm):
    name = forms.CharField(
        label="用户名",
        widget=forms.TextInput
    )

    pwd = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required= True
    )

    checkcode = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True,
    )

    class Meta:
        model = UserInfo
        fields =['name', 'pwd', 'checkcode']

    # def clean_pwd(self):
    #     return md5(self.cleaned_data['pwd'])



def login(request):
    if request.method == 'GET':
        form = UserLoginForm
        return render(request, "login.html", {"form": form})

    print(request.POST)
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        user_input_code = form.cleaned_data.pop('checkcode')
        row_object = UserInfo.objects.filter(**form.cleaned_data).first()
        #print(row_object)
        if not row_object:
            form.add_error("pwd", "用户名或密码错误")
            return render(request, "login.html", {"form": form})

        code = request.session.get("img_code")
        #print(form.cleaned_data['checkcode'])
        if code != user_input_code.upper():
            form.add_error("checkcode", "验证码错误")
            return render(request, 'login.html', {"form": form})

    #保存session 信息
    request.session.clear()
    request.session["info"] = {"id": row_object.id,  "name": row_object.name}
    request.session.set_expiry(60 * 60 * 24)
    return render(request, 'index.html')


#
def logout(request):
    request.session.clear()
    form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


#
def img_code(request):
    img, code_string = check_code()
    request.session['img_code'] = code_string
    print(code_string)
    stream = BytesIO()
    img.save(stream, 'png')
    request.session.set_expiry(60)
    return HttpResponse(stream.getvalue())
