from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="序号")
    username = models.CharField(max_length=255,verbose_name="用户名")
    password = models.CharField(max_length=255,verbose_name="密码")
    sex = models.CharField(max_length=10,verbose_name="性别")
    phone = models.CharField(max_length=255,verbose_name="手机号")
    trueName = models.CharField(max_length=255,verbose_name="真实姓名")
    auth = models.CharField(max_length=255,verbose_name="角色")
    position = models.CharField(max_length=255,verbose_name="职位",null=True,blank=True)
    headpic = models.CharField(max_length=255,verbose_name="头像地址",null=True,blank=True)

class Visit(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="序号")
    count = models.CharField(default="0",max_length=255)