from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from django.urls import reverse

from .models import BookInfo


def index(request):
    response = HttpResponse('hello,xiaobai')
    response.set_cookie('best2','python3',max_age=3000)
    response.set_cookie('best5','python6',max_age=3000)

    cookie2 = request.COOKIES.get('best2')
    print(cookie2)
    cookie3 = response.delete_cookie('best2')

    return response


def booklist(request):
    url = reverse('book:test')
    # books = BookInfo.objects.all()
    # print(books)
    # context= {
    #     'books':books
    # }
    # return render(request,'booklist.html',context=context)
    print(url)
    return HttpResponse('test233')


import json
def intex(request,value2,value1):
    print(value1,value2)
    context1 = {
        'v1': value1,
        'v2': value2,
    }
    # context=json.loads(context1)
    return render( request,'index.html', context1)


def post(request,value1,value2):
    # a = request.POST.get('a')
    # alist = request.POST.getlist('b')
    params = request.POST
    print(params)

    books = BookInfo.objects.all()
    contents = {'books':books}
    return render(request,'booklist.html',context=contents)


import json
def post_json(request):
    json_str = request.body
    # json_str = json_str.decode()
    print(json_str)
    req_data = json.loads(json_str)
    print(req_data)
    # print(request.META)
    response = JsonResponse(req_data)
    response.set_cookie('best1','python1',max_age=3600)
    return response

def get_headers(request):
    # print(request.META)
    return redirect('/booklist')

from redis import StrictRedis
def sessions(request):
    request.session['流浪地球'] = "吴京主演"
    session1 = request.session.get('流浪地球')
    # print(session1)
    redis_store = StrictRedis()
    redis_store.set('流浪地球',"吴京主演")
    sr = StrictRedis()
    result = sr.get('流浪地球')
    result=result.decode('utf8')
    print(result)
    return HttpResponse('2019大年初一')

