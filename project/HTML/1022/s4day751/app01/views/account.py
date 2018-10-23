#__author__:asus
#date:2018/10/22
from django.shortcuts import render,HttpResponse,redirect
from app01 import models
def login(req):
    if req.method=='GET':
        return render(req,'login.html')
    else:
        user=req.POST.get('username')
        pwd=req.POST.get('password')
        gender=req.POST.get('gender')
        rmb=req.POST.get('rmb')
        if gender=="1":
            obj=models.Boy.objects.filter(username=user,password=pwd).first()
        else:
            obj=models.Girl.objects.filter(username=user,password=pwd).first()
        if not obj:#如果不存在此键值对，即不存在此账户名和密码
            return render(req,'login.html',{'msg':'用户名或密码错误'})
        else:
            # req.session['user_id']=obj.id
            # req.session['gender']=gender
            # req.session['username']=user
            req.session['user_info']={'user_id':obj.id,'gender':gender,'username':user,'nickname':obj.nickname}
            return redirect('/index.html')

def logout(request):
    #删除数据库中的session
    #request.session.delete(request.session.session_key)
    #删除电脑端的session
    request.session.clear()
    return redirect('/login.html')
