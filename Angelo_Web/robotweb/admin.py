

from django.contrib import admin
from robotweb import models
from robotweb.models import Article


class ArticleInline(admin.TabularInline): #StackedInline所有列字段竖放，TabularInline所有列字段横放
    model = Article
    # raw_id_fields = ("id",)
    # extra = 3 #默认显示条目的数量
class AccountAdmin(admin.ModelAdmin):
    #主表和子表两个页面显示
    list_display = ('username','email','signature')
    search_fields = ('username','email')
    list_filter = ('username','email')
    list_per_page = 5
    list_display_links =['email',]
    list_editabel=['signature',]

    # 主表和子表一个页面显示（应用于一对多）
    inlines = [ArticleInline, ]  # Inline把ArticleInline关联进来


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','account','get_tags')
    list_fiter =('account','pub_date')
    date_hierarchy = 'pub_date'

    fieldsets = (
        ('文章内容' , {
            'fields' : ['title' , 'content'] ,
            'classes' : ('wide' , 'extrapretty') ,
        }) , (
            '发布相关' , {
                'classes': ('collapse',),
                'fields': ('account', 'tags', ('pub_date', 'read_count'))
            }
        )
    )
class TagAdmin(admin.ModelAdmin):
    list_display = ['name','colored_name']



admin.site.register(models.Account,AccountAdmin)
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Tag,TagAdmin)
# admin.site.register(ArticleInline)

admin.site.site_header = '财务主数据管理系统'
admin.site.site_title = 'Hello World'