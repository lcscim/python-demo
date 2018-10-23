from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.
def test(req):
    # boy=models.UserInfo.objects.filter(gender=1,id=2).first()
    # girl=models.UserInfo.objects.filter(gender=2,id=6).first()
    #
    # models.U2U.objects.create(b_id=boy.id,g_id=girl.id)
    # models.U2U.objects.create(b_id=2,g_id=6)
    # models.U2U.objects.create(b_id=1,g_id=6)
    # models.U2U.objects.create(b_id=1,g_id=4)
    # models.U2U.objects.create(b_id=1,g_id=5)
    xz=models.UserInfo.objects.filter(id=1).first()
    result=xz.girls.all()
    for u in result:
        print(u.g.nickname)
    return HttpResponse('...')
