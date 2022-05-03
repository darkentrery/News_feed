from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, ListView


class NewsDetailView(DetailView):
    model = Article
    template_name = 'feed/details_view.html'
    context_object_name = 'article'


class NewListView(ListView):
    paginate_by = 2
    model = Article
    template_name = 'feed/class_index.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
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
