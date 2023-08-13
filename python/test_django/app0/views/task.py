from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def task_list(request):

    return render(request, 'test_ajax.html')


@csrf_exempt
def task_ajax(request):

    print(request.GET)
    print(request.POST)
    data_dict={'status': 0, 'data':[12,3,4,9,56]}
    return JsonResponse(data_dict)