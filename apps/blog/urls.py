# coding=utf-8
from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    url(r'^articles$', views.articles, name='articles'),
    url(r'^articles/([0-9]{4})$', views.articles_year, name="someYear"),
    url(r'^articles/([0-9]{4})/([0-9]{2})$', views.articles_month, name="someMonth"),

    # 正则处理
    url(r'^news$', views.news, name="news"),
    url(r'^news/(?P<year>[0-9]{4})$', views.news_year, name="newsYear"),
    url(r'^news/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.news_month, name="newsMonth"),
    url(r'^news/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})$', views.news_day, name="newsDay"),
    url(r'^news/newDetail/(?P<id>\d{3})$', views.news_id, name="news_id"),

    # 更简洁的二级路由
    url(r'^others', include([
        url(r'^$', views.others, name="others"),
        url(r'^history$', views.others_history, name="othersHistory"),
    ])),

    url(r'^blog/page(?P<num>[0-9]+)$', views.blog, name='blog'),
    url(r'^login', views.user_login, name='login'),
    url(r'^paginator$', views.paginators, name='paginator'),
    url(r'^serializers$', views.my_serializers, name='serializers'),
    url(r'', views.index, name='index'),
]
