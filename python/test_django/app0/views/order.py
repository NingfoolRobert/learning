import random
from django.shortcuts import render,HttpResponse,redirect
from django import forms
from app0.utils.bootstrap import  BootStrapModelForm
from app0 import models
from datetime import datetime
from django.http import  JsonResponse
from app0.utils.pagination import Pagination
from django.views.decorators.csrf import csrf_exempt


#
class OrderModelForm(BootStrapModelForm):
     class Meta:
         model= models.OrderInfo
         exclude = ['oid', 'user']


#
def order_list(request):
    queryset = models.OrderInfo.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)

    print(queryset)
    form = OrderModelForm()
    context = {
        "queryset": page_object.page_queryset,
        "form": form,
        "page_string": page_object.html()
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    #print(form.cleaned_data)
    if form.is_valid():
        form.instance.oid = str(datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999)))
        form.instance.user_id = request.session["info"]['id']
        form.save()
        result = {"status": True }
        return JsonResponse(result)

    result = {
        "status": False,
        "error": form.errors
    }
    return JsonResponse(result)


def order_edit(request):
    pass

def order_delete(request):
    pass
        # form = OrderModelForm(data = request.POST)
        # form.instance.oid =

