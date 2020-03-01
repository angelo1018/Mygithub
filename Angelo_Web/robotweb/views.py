# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render,HttpResponse


# Create your views here.

def test_view(request):
    print('Hello World!',request)
    print(dir(request))
    return HttpResponse("<h1 style='color:red'>用Django封装好的HttpResponse函数返回数据到浏览器<h1>")

def test_login(request):
    return render(request,'form.html') #用render直接调用已经写好的HTML文件

def basic_selector(request):
    return render(request,'basic_selector.html')

