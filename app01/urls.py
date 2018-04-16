
from django.conf.urls import include, url
from django.contrib import admin


from app01 import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    # 位置参数：新闻查看/新闻类别/第几页
    url(r'^show_news/(\d+)/(\d+)$', views.show_news, name='show_news'),
    # 关键字参数：新闻查看/新闻类别/第几页
    url(r'^show_news2/(?P<category>\d+)/(?P<page_no>\d+)$',
        views.show_news2, name='show_news2'),

    url(r'^index1$', views.index1),

    url(r'^inherit', views.inherit, name='inherit'),
    url(r'^create_verify_code$', views.create_verify_code),
    url(r'^show_verify_codele$', views.show_verify_codele),
    url(r'^do_verify_codele$', views.do_verify_codele),
]
