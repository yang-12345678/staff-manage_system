from django.db import models


class Department(models.Model):
    """ 部门表 """
    title = models.CharField(max_length=32, verbose_name='标题')


class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    # 总长度是 10，小数点后 2 位
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")

    # 1.有约束
    # 2.django自动
    #   - 写的 depart
    #   - 生成数据库库列 depart_id
    # 3.部门表被删除
    #     3.1 级联删除，on_delete=models.CASCADE
    #     3.2 置空
    #     depart = models.ForeignKey(to="Department", to_fields="id", null=True, blank=True, on_delete=models.SET_NULL)  # 级联删除
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)  # 级联删除

    # 在django中做的约束，只能写 1 或 2
    gender_choice = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choice)
