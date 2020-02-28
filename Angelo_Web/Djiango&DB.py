# Pyhton 下用Django语法增删查改，注意创建空的数据库需要在终端或数据库软件中，表结构需要在models.py模块

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Angelo_Web.settings")# project_name 项目名称
django.setup()
from robotweb import models


# #****整表操作
o = models.Article.objects.all() # 相当于"select * from Article;"
o1 = models.Account.objects.select_related().all()
print(o.count())  #相当于 "select count(*) from Article"
print(o.filter(title__contains='的')) #相当于"select * from Article where title like "%的%""

#*****行内操作
for i in o:
#*** 取many to many 关联表值方法
    #方法一
    print(type(i.tags.all()))
    n = i.tags.all().count()
    m = 0
    while m < n:
        print(i.tags.all()[m],end='')
        m = m+1

    #方法二
    m = i.tags.all() #相当于 select_related * from Tag where Article.id = i
    print(type(m))
    print(','.join([n.name for n in i.tags.all()])) #如何在Queryset中取出不带表名的字段值
    print(','.join([str(n.id) for n in m]))

    print(i.serializable_value('title')) #从指定i行'title'列中取的数字
    print(i.title.startswith('H'))
#*** 取many to one 关联值方法
    #方法一
    x = i.serializable_value('account')
    y = models.Account.objects.get(id=x).username
    # print(type(x))
    print(x)
    print(y)
for i in o1:
    #方法二(推荐)
    x = i.username
    print(type(x))
    print(x)



# Pyhton 下用Django语法对DB中视图进行查询，注意创建空的数据库视图需要在终端或数据库软件中，视图结构需要在mysql_view_models.py模块对应重建

# *** 如何在python下取出数据库的视图 注意:1、python默认会在models中的每个表或视图结构加上ID号，所以数据库对应视图一定要包含该字段
# *** 2、有datetiem字段的要在setting.py中排除时区影响，把TZ=True改成TZ=False
from robotweb import mysql_view_models

o2 = mysql_view_models.ArtilceAuthorInfo.objects.all()

print(o2.count())
print(o2.values())
print(o2.values_list())
# o3 = o2.filter(content__contains='平台')

for i in o2:

    print((i.serializable_value('title')),i.serializable_value('name'))


print(o2.filter(title__contains='我们'))



