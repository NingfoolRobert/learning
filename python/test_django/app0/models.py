from django.db import models

# Create your models here.

#python ./manage.py makemigrations
#python ./manage.py migrate


class Department(models.Model):
    """部门表"""
    name = models.CharField(max_length=64, null=False, unique=True)
    memo = models.CharField(max_length=256)


class UserInfo(models.Model):
    """用户表"""
    name = models.CharField(max_length=20, null=False)
    pwd = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=128, null=False, unique=True)
    phone = models.CharField(max_length=11)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    #depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE) #级联删除
    department = models.ForeignKey(to="Department", to_field="id", null=True, blank=True,on_delete=models.SET_NULL) #置空

    gender_choices =(
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, default=1)


class FileInfo(models.Model):
    name = models.CharField(max_length=256, null=False)
    type_choices = (
         (1, '可执行文件'),
         (2, 'Config'),
         (3, 'shell'),
         (4, 'Python'),
         (5, 'Java'),
         (6, 'bat'),
         (7, '动态库'),
    )
    type = models.SmallIntegerField(default=0, choices=type_choices)
    size = models.IntegerField(default=0)
    version = models.IntegerField(default=0)
    md5 = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to='UserInfo', to_field='id', blank=True, null=True, on_delete=models.SET_NULL)


class TaskInfo(models.Model):
    type = models.SmallIntegerField(default=0)

    status_choices = (
         (0, '取消'),
         (1, '已完成'),
         (2, '执行中'),
         (3, '未开始'),
     )
    status = models.SmallIntegerField(default=0, verbose_name='任务状态')
    err_code_choices = (
         (0,  '成功'),
         (1,  '失败'),
    )
    err_code = models.SmallIntegerField(default=0, verbose_name='任务知行结果')
    err_msg = models.CharField(max_length=512)
    target_ip = models.CharField(max_length=16)
    target_dir = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now=True,  verbose_name='创建时间')
    schedule_time = models.DateTimeField(auto_now=True, verbose_name='计划执行时间')
    finish_time = models.DateTimeField(auto_now=True, verbose_name='完成时间')

    memo = models.CharField(max_length=512)


class TaskDtlInfo(models.Model):
    status_choices = (
        (0, '未进行'),
        (1, '进行中'),
        (2, '已完成')

    )
    status = models.SmallIntegerField(default=0, blank=False, choices=status_choices)
    opt_choices = (
         (1, '上传'),
         (2, '执行'),
    )
    #
    opt = models.SmallIntegerField(default=0, blank=True, choices=opt_choices)
    create_time = models.DateTimeField()
    schedule_time = models.DateTimeField()
    opt_time = models.DateTimeField(auto_now_add=True)
    target_ip = models.CharField(max_length=16)
    target_dir = models.CharField(max_length=256)
    args = models.CharField(max_length=256, null=True, blank=True)
    seq = models.IntegerField(default=0)
    file = models.ForeignKey(to="FileInfo",  to_field='id',blank=True, null=True,  on_delete=models.SET_NULL)
    task = models.ForeignKey(to="TaskInfo", to_field='id', on_delete=models.CASCADE)
#
#
#
#




