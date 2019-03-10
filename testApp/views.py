from django.shortcuts import render
from django.http import *
import re

def index(request):
    return render(request, "index.html")
# Create your views here.

def upload(request):
    return render(request,'upload.html')

def upload2(request):
    return render(request,'upload2.html')

def show(request):
    return render(request,'show.html')
def show2(request):
    return render(request,'show2.html')
def show3(request):
    return render(request,'show3.html')
def upload_file(request):
    username = request.POST.get('username')
    fafafa = request.FILES.get('fafafa')

    import os
    img_path = os.path.join('static/image/',fafafa.name)    #存储的路径
    with open(img_path,'wb') as f:      #图片上传
        for item in fafafa.chunks():
            f.write(item)

    ret = {'code': True , 'data': img_path}  #'data': img_path 数据为图片的路径，
    import json
    from django.shortcuts import HttpResponse
    return HttpResponse(json.dumps(ret))    #将数据的路径发送到前端

def getJS(request, path):
    with open('./js/'+path, encoding='UTF-8') as file:
        html = file.read()
        return HttpResponse(html)
def getCSS(request, path):
    with open('./css/'+path, encoding='UTF-8') as file:
        html = file.read()
        return HttpResponse(html)
def getPath(request, path):
    if re.match(path,r".html")!=None:
        return render(request, "index.html")
    with open('./testApp/'+path, encoding='UTF-8') as file:
        html = file.read()
        return HttpResponse(html)

def getHtml(request, path):
    with open('./testApp/templates'+path, encoding='UTF-8') as file:
        html = file.read()
        return HttpResponse(html)
def getImage(request, path):
    with open('./images/'+path, mode='rb') as file:
        html = file.read()
        return HttpResponse(html, content_type="image/jpeg")