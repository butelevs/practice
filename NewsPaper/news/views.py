from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post
from pprint import pprint


class NewsList(ListView):
    model = Post
    ordering = '-time_date'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # pprint(context)
        context['next_news'] = None
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'new'
