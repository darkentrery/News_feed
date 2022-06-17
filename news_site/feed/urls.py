
from django.urls import path, re_path
from . import views


urlpatterns = [
    # path('', views.index, name='home'),
    path('about', views.ArticleAPIList.as_view(), name='about'),
    path('create', views.CreateNewsView.as_view(), name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    # path('<int:pk>', views.articles_detail, name='news_detail'),
    path('', views.NewListView.as_view(), name='home'),
    re_path(r'^api/articles/$', views.ArticleAPIList.as_view()),
	re_path(r'^api/articles/(?P<pk>[0-9]+)$', views.ArticletDetail.as_view()),
]
