#__author__:asus
#date:2018/10/22
from django.shortcuts import redirect,render,HttpResponse
from app01 import models

def index(req):
    if not req.session.get('user_info'):
        return redirect('/login.html')
    else:
        gender=req.session.get('user_info').get('gender')
        if gender=='1':
            user_list=models.Girl.objects.all()
        else:
            user_list=models.Boy.objects.all()
        return render(req,'index.html',{'user_list':user_list})

def others(req):
    current_user_id=req.session.get('user_info').get('user_id')
    gender=req.session.get('user_info').get('gender')
    if gender=='1':
        user_list=models.B2G.objects.filter(b_id=current_user_id).values('g__nickname')
    else:
        user_list=models.B2G.objects.filter(g_id=current_user_id).values('b__nickname')
    return render(req,'others.html',{'user_list':user_list})