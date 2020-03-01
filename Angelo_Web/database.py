# Pyhton 下用Django语法增删查改，注意创建空的数据库需要在终端或数据库软件中，表结构需要在models.py模块

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Angelo_Web.settings")# project_name 项目名称
django.setup()
from robotweb import models
import datetime
# 创建表记录
# new_user_obj = models.Account.objects.create(
#     username='alex',
#     email='alex@luffycity.com',
#     password='abc123',
#     signature='chaos is a ladder'
# )
# new_user_obj.save()

obj = models.Article.objects.create(
    title="'后来的我们'学会了造假",
    content="'后来的我们'...答案揭晓--刷票房刷来的",
    account_id=4,
    pub_date=datetime.datetime.now()
)
#
obj.tags.add(1,2)