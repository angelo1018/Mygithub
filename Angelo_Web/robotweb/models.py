# 通过此文件：
# 1、制作生成migrations下0001_initial.py文件，生成同步文件命令：python manage.py makemigrations
# 2、同步文件到数据库，对应命令：python manage.py migrate,在数据库中生成相应表
from django.db import models

from django.utils.html import format_html

# Create your models here.


class Account(models.Model):
    """账户表"""

    username = models.CharField("用户名",max_length=64,unique=True)
    email = models.EmailField("电子邮件")
    password = models.CharField("密码",max_length=255,blank=True)
    register_date = models.DateTimeField("登记时间",auto_now_add=True)
    signature = models.CharField("签名",max_length=255,null=True,blank=True)
    gender = models.TextChoices("性别",)

    #article_set = Article
    def __str__(self):
        return self.username+"(笔名:"+self.signature+")"
    class Meta:
        #verbose_name = "文章"
        verbose_name_plural = "作者"


class Article(models.Model):
    """文章表"""

    title = models.CharField("标题",max_length=255,unique=True)
    content = models.TextField("内容")
    account = models.ForeignKey("Account",on_delete=models.CASCADE)
    account.verbose_name = u'用户名'
    tags = models.ManyToManyField("Tag",null=True,blank=True)
    pub_date = models.DateField("发表日期")
    read_count = models.IntegerField(verbose_name="阅读",default=0)



    class Meta:
        #verbose_name = "文章" #针对英文，界面会自动显示"文章s"
        verbose_name_plural = "文章" #不想显示复数用此命令


    def get_tags(self):
        return  ','.join([i.name for i in self.tags.all()])
    get_tags.short_description = u'标签'

    def get_comment(self):
        return 10


    def __str__(self):
        return "%s - %s " %(self.title,self.account)


class Tag(models.Model):
    """标签表"""
    name = models.CharField('名称',max_length=64,unique=True)
    date = models.DateTimeField(auto_now_add=True)
    color_code = models.CharField(max_length=6)


    def colored_name(self):
        return format_html('<span style="color: #{};">{}</span>',self.color_code,self.name,
        )

    colored_name.short_description = u"颜色"

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "标签"

