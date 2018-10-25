#__author__:asus
#date:2018/10/25
from django.shortcuts import HttpResponse,redirect,render

from django.forms import Form
from django.forms import fields
import json

# class LoginForm(Form):
#
#     username=fields.CharField(
#         max_length=24,
#         min_length=6,
#         required=True,
#         error_messages={
#             'required':'用户名不能为空',
#             'min_length':'太短了',
#             'max_length':'太长了',
#         }
#     )
#     password=fields.CharField(max_length=24,required=True)
#
# def login(req):
#
#     if req.method=='GET':
#         return render(req,'login.html')
#     else:
#         #进行验证
#         obj=LoginForm(req.POST)
#         if obj.is_valid():#如果验证通过is_valid返回TRUE
#             print(obj.cleaned_data)#返回数据的字典类型
#             return redirect('http://www.baidu.com')
#         else:
#             return render(req,'login.html',{'obj':obj})

# class LoginForm(Form):
#     user=fields.CharField(required=True)
#     pwd=fields.CharField(min_length=18)
#     # t1=fields.IntegerField()自带正则表达式
#     # t2=fields.EmailField()
#     # t3=fields.URLField()
#     # t3=fields.RegexField('139\d+')自定正则表达式
#
# def login(req):
#     if req.method=='GET':
#         return render(req,'login.html')
#     else:
#         obj=LoginForm(req.POST)
#         if obj.is_valid():
#             print(obj.cleaned_data)
#             return redirect('http://www.baidu.com')
#         # else:
#         #     print(obj.errors)
#         return render(req,'login.html',{'obj':obj})
#
# def ajax_login(req):
#     ret={'status':True,'msg':None}
#     obj=LoginForm(req.POST)
#     if obj.is_valid():
#         print(obj.cleaned_data)
#     else:
#         ret['status']=False
#         ret['msg']=obj.errors
#         # print(obj.errors)
#     v=json.dumps(ret)
#     return HttpResponse(v)

class TestForm(Form):
    t1=fields.CharField(max_length=12)
    t2=fields.CharField(max_length=12)

def test(req):
    if req.method=='GET':
        obj=TestForm()
        return render(req,'test.html',{'obj':obj})
    else:
        obj=TestForm(req.POST)
        if obj.is_valid():
            return HttpResponse('...')
        else:
            return render(req,'test.html',{'obj':obj})