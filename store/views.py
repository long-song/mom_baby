from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    访问首页
    :param request:
    :return:
    '''
    return render(request,'index.html')

def login(request):
    '''
    访问登录页面
    :param request:
    :return:
    '''
    return render(request,'login.html')