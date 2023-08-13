from django.db import models

# Create your models here.

#python ./manage.py makemigrations
#python ./manage.py migrate


class Department(models.Model):
    """部门表"""
    name = models.CharField(max_length=64, null=False, unique=True)
    parent_id = models.ForeignKey(to="Department",to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    memo = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    """用户表"""
    name = models.CharField(max_length=20, null=False, verbose_name="用户名")
    pwd = models.CharField(max_length=64, null=False, verbose_name="密码")
    email = models.EmailField(max_length=128, null=False, unique=True, verbose_name="邮箱")
    phone = models.CharField(max_length=11, verbose_name="手机号")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    #depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE) #级联删除
    department = models.ForeignKey(verbose_name="部门",to="Department", to_field="id", null=True, blank=True,on_delete=models.SET_NULL) #置空

    gender_choices =(
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, default=1)

    def __str__(self):
        return self.name


class FileInfo(models.Model):
    name = models.CharField(max_length=256, null=False, verbose_name="文件名")
    type_choices = (
         (1, '可执行文件'),
         (2, 'Config'),
         (3, 'shell'),
         (4, 'Python'),
         (5, 'Java'),
         (6, 'bat'),
         (7, '动态库'),
    )
    type = models.SmallIntegerField(default=0, choices=type_choices, verbose_name="类型")
    size = models.IntegerField(default=0, verbose_name="大小")
    version = models.IntegerField(default=0, verbose_name="版本")
    md5 = models.CharField(max_length=64, verbose_name="MD5")
    create_time = models.DateTimeField(null=True, verbose_name="创建时间")
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
    path = models.CharField(verbose_name="路径", max_length=256, null=True, blank=True)
    user = models.ForeignKey(verbose_name="发布者", to='UserInfo', to_field='id', blank=True, null=True, on_delete= models.SET_NULL)


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
    status = models.SmallIntegerField(default=0, blank=False, choices=status_choices, verbose_name="执行状态")
    opt_choices = (
         (1, '上传'),
         (2, '下载'),
         (2, '执行'),
    )
    #
    opt = models.SmallIntegerField(default=0, blank=True, choices=opt_choices, verbose_name="任务类型")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    schedule_time = models.DateTimeField(verbose_name="计划时间", auto_now=False, null=True)
    opt_time = models.DateTimeField(verbose_name="执行时间", auto_now_add=False, null=True)
    target_ip = models.CharField(verbose_name="机器IP",max_length=16)
    target_dir = models.CharField(verbose_name="目标路径", max_length=256)
    args = models.CharField(verbose_name="命令", max_length=256, null=True, blank=True)
    seq = models.IntegerField(verbose_name="任务编号", default=0)
    file = models.ForeignKey(verbose_name="文件", to="FileInfo",  to_field='id', blank=True, null=True,  on_delete=models.SET_NULL)
    task = models.ForeignKey(verbose_name="父任务", to="TaskInfo", to_field='id', on_delete=models.CASCADE)
#
#
#
#


class OrderInfo(models.Model):
    oid = models.CharField(verbose_name="订单号", max_length=128, null=False, blank=False)
    name = models.CharField(verbose_name="名称", max_length=128, null=False, blank=False)
    status_choices=(
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    price = models.DecimalField(verbose_name="价格", decimal_places=2, max_digits=10, default=0.0)
    create_time= models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    user = models.ForeignKey(verbose_name="用户", to="UserInfo", on_delete=models.CASCADE)




