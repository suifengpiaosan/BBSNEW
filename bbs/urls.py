# -*- coding: utf-8 -*-
# @Time    : 2017\11\30 0030 11:35
# @Author  : Rain
# @Email   : huaeryijiukai@gmail.com
# @File    : urls.py.py
# @Software: PyCharm
from django.conf.urls import url,include
from bbs import views
urlpatterns = [

    url(r'^$',views.index),
    url(r'^category/(\d+)/$',views.category),
]
