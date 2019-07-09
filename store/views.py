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

def list(request):
    '''
    访问商品列表页面
    :param request:
    :return:
    '''
    return render(request,'commodity.html')

def buytoday(request):
    '''
    访问今日团购页面
    :param request:
    :return:
    '''
    return render(request,'buytoday.html')

def information(request):
    '''
    访问母婴资讯页面
    :param request:
    :return:
    '''
    return render(request,'information.html')

def shopcart(request):
    '''
    访问购物车页面
    :param request:
    :return:
    '''
    return render(request,'shopcart.html')

def about(request):
    '''
    访问关于我们页面
    :param request:
    :return:
    '''
    return render(request,'about.html')

def details(request):
    '''
    访问产品详情页面
    :param request:
    :return:
    '''
    return render(request,'details.html')