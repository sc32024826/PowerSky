from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # 参数1: 携带的参数  参数2:对应的方法名,参数3: 全局变量名
    path('', views.index, name='HomeView'),    # 首页
    path('manage/', views.message, name='manage'),    # 总经理致辞
    path('story/', views.story, name='story'),      # 品牌故事
    path('social/', views.social, name='social'),   # 社会责任
    path('develop/', views.develop, name='develop'),    # 发展历程
    path('culture/', views.culture, name='culture'),    # 企业文化
    path('hr/', views.hr, name='hr'),   # 人力资源
    path('honor/', views.honor, name='honor'),      # 企业荣誉
    path('products/<int:type_num>/', views.products, name='ProductView'),   # 根据产品分类显示产品
    path('products/', views.all_products, name='allProductView'),   # 显示所有产品
    path('detail/<int:pk>/', views.detail, name='detail'),      # 产品详情页
    path('solution<int:pk>/', views.solution, name='solution'),     # 解决方案 详情
    path('solution_list', views.solution_list, name='solution_list'),   # 解决方案列表
    path('solution/classify/<int:classify>/', views.solution_class, name='solution_class'),   # 解决方案分类
    path('news/detail/<int:pk>/', views.news_detail, name='new_detail'),  # 新闻详情
    path('news/<int:news_type>/', views.news_view, name='news'),    # 新闻中心
    path('business/', views.business, name='business'),      # 招商页面
    path('contact/', views.contact, name='contactUs'),  # 联系我们
    path('servers/', views.service, name='service'),    # 服务理念


    path('process/', views.submit_process, name='submit'),     # 前台表单提交
    path('list/', views.MyListView.as_view(), name='admin_joinList'),     # 后台输出加盟列表


]
