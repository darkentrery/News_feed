from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Articles
from .forms import ArticleForm




def index(request):
    news = Articles.objects.order_by('-date')
    data = {'news': news}
    return render(request, 'feed/index.html', data)

def create(request):
    form = ArticleForm()
    data = {
        'form': form
    }
    return render(request, 'feed/create.html', data)


def about(request):
    return render(request, 'feed/index.html')