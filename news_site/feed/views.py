from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Articles
from .forms import ArticleForm
from django.views.generic import DetailView, ListView


class NewsDetailView(DetailView):

    model = Articles
    template_name = 'feed/details_view.html'
    context_object_name = 'article'


class NewListView(ListView):
    paginate_by = 2
    model = Articles
    template_name = 'feed/class_index.html'
    context_object_name = 'article'


def index(request):
    order_news = Articles.objects.order_by('id')
    news = Articles.objects.order_by('-date')
    data = {'news': news, 'order_news': order_news}
    return render(request, 'feed/index.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Incorrect form"
    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'feed/create.html', data)


def about(request):
    return render(request, 'feed/index.html')
