from django.shortcuts import render


def test_md5(request):

    return render(request, 'test_md5.html')