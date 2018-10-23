from django.db import models

class UserInfo(models.Model):
    nickname=models.CharField(max_length=32)
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    gender_choices={
        (1,'男'),
        (2,'女'),
    }
    gender=models.IntegerField(choices=gender_choices)

# 反向操作时会造成冲突
#obj对象男是u2u_set.all(),女是u2u_set.all()
#解决办法related_query_name
#此时就是a_set.all()  男 b_set.all()
# 或者related_name
# 此时就是a.all()  男 b.all()
class U2U(models.Model):
    g=models.ForeignKey('UserInfo',on_delete=models.CASCADE,related_name='boys')
    b=models.ForeignKey('UserInfo',on_delete=models.CASCADE,related_name='girls')


