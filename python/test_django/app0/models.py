from django.db import models

# Create your models here.

#python ./manage.py makemigrations
#python ./manage.py migrate

class Department(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True)
    memo = models.CharField(max_length=256)


class UserInfo(models.Model):
    name = models.CharField(max_length=20, null=False)
    pwd = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=128, null=False, unique=True)
    phone = models.CharField(max_length=11)

class FileInfo(models.Model):
     name = models.CharField(max_length=256, null=False,  blank=False)
     type = models.IntegerField(default=0)
     size = models.IntegerField(default=0)
     version = models.IntegerField(default=0)
     md5 = models.CharField(max_length=64)
     create_time = models.DateTimeField()


class TaskInfo(models.Model):
     type = models.IntegerField(default=0)



class TaskDtlInfo(models.Model):
     opt  = models.SmallIntegerField(default=0)
     create_time = models.DateTimeField()
     stat   = models.SmallIntegerField()
     schedule_time = models.DateTimeField()
     opt_time   = models.DateTimeField(auto_now_add=True)
     target_ip = models.CharField(max_length=16)
     dir = models.CharField(max_length=256)
#
#
#
#




