from django.shortcuts import render, HttpResponse,redirect


# Create your views here.


def index(request):
    return render(request, 'index.html')

def user_add(request):
    return render(request, 'user_add.html')



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

    if name == 'root' and pwd == '123':
        return redirect("/index")

    return render(request, 'login.html',  {"error_msg":"用户名或密码错误"})