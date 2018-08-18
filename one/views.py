from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from one.models import log
import requests
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class Login(View):
    def get(self,request):
        return render(request, 'login.html', {})
    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/index/')

        else:
            return render(request, 'login.html', {})

@login_required
def Index(request):

    if request.method == "POST":
        return render(request,'generic.html',{})

    if request.method == 'GET':
        log_id = None
        try:
            log_id = int(request.GET.get('id'))
        except:
            pass
        if log_id:
            message = log.objects.get(id=log_id)
            all = log.objects.all()
            all = reversed(all)
            return render(request,'generic.html',{'all':all,'message':message})
        else:
            message = log.objects.latest('id')
            all = log.objects.all()
            all = reversed(all)
            return render(request,'generic.html',{'all':all,'message':message})

@login_required
def Ele(request):

    if request.method == "GET":
        return render(request,'elements.html',{})

    if request.method == "POST":
        title = request.POST.get('title')
        message = request.POST.get('message')
        img = request.FILES.get('img')
        log.objects.create(tittle=str(title),text=str(message),pic=img)
        all = log.objects.all()
        all = reversed(all)
        new = log.objects.latest('id')
        return render(request,'generic.html',{'all':all,'message':new})

class robot(View):
    def get(self,request):
        if request.is_ajax():
            s = request.GET.get('text')
            resp = requests.post("http://www.tuling123.com/openapi/api",
                                 data={"key": "dc5ab666b49d4d54af2d90fb147628f7", "info": s, })
            resp = resp.json()
            dic = {'big':str(s),'small':str(resp['text'])}
            return JsonResponse(dic)
        else:
            return render(request,'robot.html',{})

