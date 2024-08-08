from django.urls import path

# from hexlet_django_blog.article import views
from hexlet_django_blog.article import views

urlpatterns = [
    # path('', views.index),
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<str:tags>/<int:article_id>', views.IndexView.as_view(),
         name='article'),
    # path('<str:tags>/<int:article_id>', views.index),
    path('<int:article_id>', views.ArticleView.as_view(),
         name='articles_detail'),
    path('create', views.ArticleCreateView.as_view(), name='articles_create'),
]
