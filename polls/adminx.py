import xadmin
from .models import Products, MyNews, JoinUs, JobRequire, Banner


class PAdmin(object):
    list_display = ['name', 'type_text']
    style_fields = {'context': 'ueditor'}
    model_icon = 'fa fa-truck'


class JoinAdmin(object):
    list_display = ['Product', 'name', 'area', 'tel']
    model_icon = 'fa fa-vcard'


class NewsAdmin(object):
    list_display = ['tt', 'logo', 'read_count', 'author', 'date']
    style_fields = {'context': 'ueditor'}
    model_icon = 'fa fa-newspaper-o'


class JobStyle(object):
    list_display = ['jobName', 'needCount', 'workPlace', 'education', 'workYears']
    model_icon = 'fa fa-info'


class BAdmin(object):
    list_display = ['url']
    model_icon = 'fa fa-image'


xadmin.site.register(Products, PAdmin)          # 产品
xadmin.site.register(JoinUs, JoinAdmin)         # 客户
xadmin.site.register(MyNews, NewsAdmin)         # 新闻
xadmin.site.register(JobRequire, JobStyle)      # 岗位
xadmin.site.register(Banner, BAdmin)            # banner

