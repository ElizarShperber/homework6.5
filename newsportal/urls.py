
from django.contrib import admin
from django.urls import path, include

from newsportal.views import NewsListView, NewsDetailView

urlpatterns = [

    path('news/', NewsListView.as_view(), name= 'news_all'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_single'),

]
