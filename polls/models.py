from django.db import models
from DjangoUeditor.models import UEditorField


# 产品数据库
# id,name
# src:产品图片地址
# date:文章编写日期
# read_count:文章阅读次数
# author:作者
# context:文章主体
# type_num:产品分类号
# effect:作用简介
# type_text:产品型号
# is_solu: 是否为解决方案,1:是解决方案,0:是产品
# classify: 解决方案的分类号 0:无效,1:SCR系统解决方案 ,2:燃油系统解决方案,3:润滑系统决方案,4:EGR系统解决方案
class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='产品名称')
    src = models.ImageField(
        upload_to="org/%Y/%m",
        default='org/2019/08/ico.png',
        verbose_name="产品图片")
    date = models.DateField('编写日期')
    read_count = models.IntegerField(default=0, verbose_name='阅读量')
    author = models.CharField(max_length=100, verbose_name='作者')
    context = UEditorField(
        width=1200,
        height=600,
        toolbars='full',
        imagePath='img/',
        upload_settings={
            'imageMaxSize': 1204000
        },
        settings={},
        verbose_name='内容'
                           )
    type_num = models.IntegerField(default=0, verbose_name='产品分类号,0:车用尿素,1:加注设备')
    effect = models.CharField(max_length=100, verbose_name='产品作用简介', null=True, blank=True)
    type_text = models.CharField(max_length=50, verbose_name='产品型号', null=True, blank=True)
    is_solu = models.IntegerField(default=0, verbose_name='是否为解决方案,1:是解决方案,0:是产品')
    classify = models.IntegerField(default=0, verbose_name='解决方案的分类号 0:无效,1:SCR系统解决方案 ,2:燃油系统解决方案,3:润滑系统决方案,4:EGR系统解决方案')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']


# 新闻类数据库
# tt: 文章标题
# date:文章编写日期
# read_count:文章阅读次数
# author:作者
# context:文章主体
# logo:文章图片地址
# news_type: 新闻类型
class MyNews(models.Model):
    tt = models.CharField(max_length=100, verbose_name='新闻标题')
    date = models.DateField('编写日期')
    read_count = models.IntegerField(default=0, verbose_name='阅读量')
    author = models.CharField(max_length=100, verbose_name='作者')
    context = UEditorField(
        width=1200,
        height=600,
        toolbars='full',
        imagePath='img/',
        upload_settings={
            'imageMaxSize': 1204000
        },
        settings={},
        verbose_name='内容'
                           )
    logo = models.ImageField(
        upload_to="org/%Y/%m",
        default='',
        verbose_name="新闻图片")
    news_type = models.IntegerField(default=0, verbose_name='新闻类别')

    def __str__(self):
        return self.tt

    class Meta:
        ordering = ['date']


# 加盟信息表单
class JoinUs(models.Model):
    Product = models.CharField(max_length=100, verbose_name='产品名称')      # 产品
    area = models.CharField(max_length=100, verbose_name='地区')         # 地区
    name = models.CharField(max_length=100, verbose_name='姓名')         # 姓名
    tel = models.CharField(max_length=11, verbose_name='电话')           # 电话

    def __str__(self):
        return self.name


# 首页banner轮播图片
class Banner(models.Model):
    url = models.ImageField(
        upload_to="banner/%Y/%m",
        default='',
        verbose_name='分辨率1920X758,非白底图片更优'
    )


# 招聘
class JobRequire(models.Model):
    jobName = models.CharField(max_length=30, verbose_name='岗位名称')
    workYears = models.PositiveSmallIntegerField(default=0, verbose_name='工作经验')
    needCount = models.IntegerField(default=1, verbose_name='招聘人数')
    workPlace = models.CharField(max_length=30, verbose_name='工作地点', default='桐乡')
    education = models.CharField(max_length=10, verbose_name='最低学历要求')
    pushData = models.DateField('发布日期')
    content = UEditorField(
        width=1200,
        height=600,
        toolbars='full',
        verbose_name='内容',
        )
