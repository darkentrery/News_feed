from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination

from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, ListView, CreateView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from .serializers import *


class ProductPagination(PageNumberPagination):
    page_size = 2


class ArticleAPIList(generics. ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ProductPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for ob in serializer.data:
                if ob['photo']:
                    # ob['photo'] = ob['photo'].replace('/media', ':1337/media')
                    print(f"{ob['photo']=}")
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        print(f"{serializer=}")
        for ob in serializer.data:
            if ob['photo']:
                # ob['photo'] = ob['photo'].replace('/media', ':1337/media')
                print(f"{ob['photo']=}")
        return Response(serializer.data)


class ArticletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(f"{pk=}")
        object = Article.objects.get(pk=kwargs['pk'])
        serializer = ArticleSerializer(object)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def articles_list(request):
    """
 List  articles, or create a new article.
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        articles = Article.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 2)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ArticleSerializer(data, context={'request': request}, many=True)
        print(f"{serializer=}")
        for ob in serializer.data:
            ob['photo'] = ob['photo'].replace('/media', ':1337/media')
            print(f"{ob['photo']=}")

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/articles/?page=' + str(nextPage), 'prevlink': '/api/articles/?page=' + str(previousPage)})

    elif request.method == 'POST':
        print(f"{request.data=}")
        serializer = ArticleSerializer(data=request.data)
        print(f"{serializer=}")
        print(f"{serializer.is_valid()=}")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def articles_detail(request, pk):
    """
    Retrieve, update or delete a article by id/pk.
 """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article, context={'request': request})

        serializer.data['photos'] = "1" #serializer.data['photo'].replace('/media', ':1337/media')
        print(f"{serializer.data=}")
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
