from django.shortcuts import render, redirect

from app01 import models


def depart_list(request):
    """ 部门列表 """

    # 去数据库中获取所有的部门列表
    # [对象，对象]
    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    """ 添加部门 """

    if request.method == "GET":
        return render(request, 'depart_add.html')

    # 获取用户 POST 提交过来的数据(title 输入为空)
    title = request.POST.get("title")

    # 保存到数据库
    models.Department.objects.create(title=title)

    # 重定向回部门列表
    return redirect("/depart/list/")
