import xadmin
from .models import Products, MyNews, JoinUs, JobRequire, Banner


class PAdmin(object):
    list_display = ['name', 'type_text']
    style_fields = {'context': 'ueditor'}


class JoinAdmin(object):
    list_display = ['Product', 'name', 'area', 'tel']


class NewsAdmin(object):
    list_display = ['tt', 'logo', 'read_count', 'author', 'date']
    style_fields = {'context': 'ueditor'}


class JobStyle(object):
    list_display = ['jobName', 'needCount', 'workPlace', 'education', 'workYears']


class BAdmin(object):
    list_display = ['url']


xadmin.site.register(Products, PAdmin)          # 产品
xadmin.site.register(JoinUs, JoinAdmin)         # 客户
xadmin.site.register(MyNews, NewsAdmin)         # 新闻
xadmin.site.register(JobRequire, JobStyle)      # 岗位
xadmin.site.register(Banner, BAdmin)            # banner

