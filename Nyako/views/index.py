import os
from django.http import  HttpResponse
from django.shortcuts import render ##小猫
def index(request):
    listdir=os.listdir("./rizhis/")
    return render(request,'index.html',locals())
def page(request,title):
    f = open("./rizhis/"+title, encoding='utf-8')
    a = {}
    a['title'] = title
    a['txt'] = f.read()
    return render(request, "rizhi.html",locals())
def date(request,year,month,day):
    return HttpResponse(f"hello Nyako,你输入了一个日期：{year}年{month}月{day}日")
def template_exampl(request):
    name='Nyako'
    eatter='电梯'
    data={'脑浆':'好吃'}
    return render(request, "public_exampl.html",locals())