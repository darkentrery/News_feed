from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, ListView, CreateView


class NewsDetailView(DetailView):
    model = Article
    template_name = 'feed/details_view.html'
    context_object_name = 'article'


class NewListView(ListView):
    paginate_by = 2
    model = Article
    template_name = 'feed/class_index.html'
    context_object_name = 'article'


class CreateNewsView(CreateView):
    template_name = 'feed/create.html'
    form_class = ArticleForm
    success_url = "/"
    model = Article


# def create(request):
#     form = ArticleForm(request.POST or None, files=request.FILES or None)
#     #if request.method == 'POST':
#         #form = ArticleForm(request.POST, request.FILES)
#     if not form.is_valid():
#         error = "Incorrect form"
#         data = {
#             'form': form,
#             'error': error
#         }
#         return render(request, 'feed/create.html', data)
#
#     form.save()
#     return redirect('home')



def about(request):
    HttpResponse()
    JsonResponse
    return render(request, 'feed/index.html')
