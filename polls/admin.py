from django.contrib import admin
from .models import Products, MyNews, JoinUs, Banner, JobRequire
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_text')


class JoinAdmin(admin.ModelAdmin):
    list_display = ('Product', 'name', 'area', 'tel')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('tt', 'logo', 'read_count', 'author', 'date')


class JobStyle(admin.ModelAdmin):
    list_display = ('jobName', 'needCount', 'workPlace', 'education', 'workYears')


admin.site.register(Products, ProductAdmin)
admin.site.register(MyNews, NewsAdmin)
admin.site.register(JoinUs, JoinAdmin)
admin.site.register(Banner)
admin.site.register(JobRequire, JobStyle)
