from django.shortcuts import render

# Create your views here.
from newsportal.models import Post
from django.views.generic import ListView, DetailView

class NewsListView(ListView):
    model=Post
    template_name = 'news_all.html'
    context_object_name = 'posts'
    ordering = ['-date_time_create']





class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_single.html'