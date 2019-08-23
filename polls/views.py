from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import Http404
from django.db.models import F
from django.http import HttpResponse
from polls.form import JoinForm
from .models import Products, MyNews, JoinUs, Banner, JobRequire
from django.views import generic
import re

# 网站默认首页


def index(request):
    # banner_list = get_list_or_404(Banner)[:5]
    try:
        banner_list = Banner.objects.all()[:5]
    except Banner.DoesNotExist:
        raise Http404("数据库不存在")

    num = len(banner_list)

    xx = range(1, num + 1)

    try:
        news = MyNews.objects.order_by('date')[:4]      # 根据日期排列 读取前4条新闻
    except MyNews.DoesNotExist:
        raise Http404("数据库不存在")

    my_list = []

    for new in news:
        # 忽略警告,必须在循环内定义,否则会覆盖所有dic
        dic = dict()
        # print(new)
        dic['id'] = new.id
        dic['logo'] = new.logo       # 获取新闻列表中单个新闻的logo图片地址
        # print(dic['logo'])
        dic['title'] = new.tt       # 获取新闻标题
        # print(dic['title'])
        # 获取新闻主要内容的首行文字,使用正则表达式 去掉html 标签
        txt = new.context.replace('&nbsp;', '')
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', txt)
        dic['text'] = dd[:60]
        # print(dic)
        my_list.append(dic)

    # print(my_list)
    main = my_list[0]
    content = {
        'title': '力众蓝天',
        'banner_list': banner_list,
        'num': xx,
        'main': main,
        'list': my_list[1:],
    }
    return render(request, 'polls/index/index.html', content)


# 总经理致辞
def message(request):
    return render(request, 'polls/index/message.html', {'title': '力众蓝天'})


# 品牌故事
def story(request):
    return render(request, 'polls/index/story.html', {'title': '品牌故事'})


# 社会责任
def social(request):
    return render(request, "polls/index/social.html", {'title': '社会责任'})


# 发展历程
def develop(request):
    return render(request, "polls/index/develop.html", {'title': '发展历程'})


# 企业文化
def culture(request):
    return render(request, "polls/index/culture.html", {'title': '企业文化'})


# hr
def hr(request):
    jobs = get_list_or_404(JobRequire)
    data = {
        'jobs': jobs,
        'title': '人力资源'
    }

    return render(request, "polls/index/HR.html", data)


# 企业荣誉
def honor(request):
    return render(request, "polls/index/honor.html", {'title': '企业荣誉'})


# 新闻中心
# news_type:新闻类别,0:自己的新闻,1:行业新闻,2:媒体报道,3:技术交流
def news_view(request, news_type):

    if news_type == 0:
        title = "力众蓝天新闻"
        news_list = get_list_or_404(MyNews, news_type=0)
    elif news_type == 2:
        title = "媒体报导"
        news_list = get_list_or_404(MyNews, news_type=1)
    elif news_type == 1:
        title = "行业新闻"
        news_list = get_list_or_404(MyNews, news_type=2)
    elif news_type == 3:
        title = "技术交流"
        news_list = get_list_or_404(MyNews, news_type=3)
    else:
        news_list = get_list_or_404(MyNews)
        title = "全部新闻"

    news_list = mypage(news_list, request)

    content = {
        'new_list': news_list,
        'type': news_type,
        'title': title,
    }
    return render(request, 'polls/news.html', content)


# 产品默认显示页,根据参数 type_num 产品类型号进行产品分类,并输出list
def products(request, type_num):
    try:
        products_list = Products.objects.filter(type_num=type_num)
    except Products.DoesNotExist:
        raise Http404("Products does not exist")

    products_list = mypage(products_list, request)

    context = {
        'products_list': products_list,
        'title': '产品页'
    }
    return render(request, 'polls/products.html', context)


# 无参 产品页  显示全部产品
def all_products(request):
    try:
        products_list = Products.objects.all()
    except Products.DoesNotExist:
        raise Http404("Products does not exist")

    products_list = mypage(products_list, request)

    context = {
        'products_list': products_list,

        'title': '产品页',
    }
    return render(request, 'polls/products.html', context)


# 产品详情页
# 显示单个产品的详细说明页
# pk 产品id号
def detail(request, pk):
    print("------------产品id %s" % pk)
    try:
        product = Products.objects.get(pk=pk)
        product.read_count = F('read_count') + 1
        product.save()
        product.refresh_from_db()
    except Products.DoesNotExist:
        raise Http404("Product does not exist")
    title = "产品详情页"
    content = {
        'product': product,
        'title': title,
    }
    print(content)
    return render(request, 'polls/detail.html', content)


# 联系页面
def contact(request):
    return render(request, 'polls/ContactUs.html')


# 新闻详情页
def news_detail(request, pk):
    try:
        new = MyNews.objects.get(pk=pk)
    except MyNews.DoesNotExist:
        raise Http404("该新闻已过期!")
    title = "新闻详情页"
    content = {
        'new': new,
        'title': title,
    }
    return render(request, 'polls/detail.html', content)


# 解决方案详情页
def solution(request, pk):
    solu = get_object_or_404(Products, pk=pk)
    title = "解决方案"
    content = {
        'product': solu,
        'title': title,
    }
    return render(request, "polls/detail.html", content)


# 解决方案 列表
def solution_list(request):
    s_list = get_list_or_404(Products, is_solu=1)     # =1 表示筛选解决方案

    print(s_list)
    if not s_list:
        raise Http404("数据为空")

    s_list = mypage(s_list, request)

    title = "解决方案列表"
    content = {
        'products_list': s_list,
        'title': title,

    }
    return render(request, "polls/products.html", content)


# 按照分类显示 解决方案
# 解决方案的分类 分为0:无效,1:SCR系统解决方案 ,2:燃油系统解决方案,3:润滑系统决方案,4:EGR系统解决方案
def solution_class(request, classify):

    products_list = get_list_or_404(Products, classify=classify)

    title = ''

    if classify == 1:   # SCR系统解决方案
        title = 'SCR系统解决方案'
    elif classify == 2:
        title = '燃油系统解决方案'
    elif classify == 3:
        title = '润滑系统决方案'
    elif classify == 4:
        title = 'EGR系统解决方案'
    products_list = mypage(products_list, request)

    content = {
        'products_list': products_list,
        'title': title,
    }

    return render(request, "polls/products.html", content)


# 招商页
def business(request):
    if request.method == 'POST':
        jon = JoinForm()
        if jon.is_valid():
            print(jon.cleaned_data)
        else:
            print(jon.errors)
    else:
        jon = JoinForm()
    content = {
        'form': jon.as_p(),
        'title': '招商加盟',
    }
    return render(request, "polls/business.html", content)


# 表单提交
def submit_process(request):
    po = request.POST
    print(po)
    # todo
    n = JoinUs()
    n.product = po.get("product_name")
    n.area = po.get("area")
    n.name = po.get("name")
    n.tel = po.get("tel")

    n.save()

    mess = {
        'title': '感谢',
        'message': '信息已经提交,感谢您的关注!',
    }

    return render(request, "polls/Tools/Message.html", mess)


# 分页处理函数
# products_list: 需要处理的list
#
def mypage(products_list, request):

    paginator = Paginator(products_list, 30)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            products_list = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            products_list = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            products_list = paginator.page(paginator.num_pages)

    return products_list


# 服务理念
def service(request):

    return render(request, "polls/service.html", {'title': '服务理念'})


# todo
# 后台页面显示 加盟信息
class MyListView(generic.ListView):
    template_name = 'admin/JoinUsList.html'

    def get_queryset(self):
        return JoinUs.objects.all()
