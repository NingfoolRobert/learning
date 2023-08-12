"""
文件管理类
"""
from django.shortcuts import render, HttpResponse,redirect
from app0.models import Department,UserInfo,FileInfo
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app0.utils.pagination import Pagination


class FileModelForm(forms.ModelForm):

    class Meta:
        model = FileInfo
        fields = ['name', 'version', 'type', 'size', 'user', 'create_time']
        # exclude = ['upload_time']
        # fields= '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            print(name, field)
            # if name == "pwd":
            #     field.widget.attrs = {"class": "form-control", "type": "password"}
            #     continue
            field.widget.attrs = {"class": "form-control"}


def file_list(request):
    data_dict = {}
    search_data = request.GET.get('query', "")
    if search_data:
        data_dict['name__contains'] = search_data
    queryset = FileInfo.objects.filter(**data_dict).order_by('id')
    page_object = Pagination(request, queryset)
    page_query = page_object.page_queryset
    page_string = page_object.html()
    return render(request, "file_list.html", {"queryset": page_query, "search_data": search_data, "page_string": page_string})


def file_add(request):
    if request.method == 'GET':
        form = FileModelForm()
        return render(request, 'file_add.html', {'form': form})

    form = FileModelForm(data= request.POST)
    if form.is_valid():
        form.save()
        return redirect('/file/list')
    return render(request, 'file_add.html', {'form': form})


def file_edit(request, fid):
    obj = FileInfo.objects.filter(id=fid).first()
    if request.method == 'GET':
        form= FileModelForm(instance=obj)
        return render(request, 'file_edit.html', {"form": form})

    form = FileModelForm(data = request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return  redirect("/file/list")

    return render(request, 'file_edit.html', {"form": form})


