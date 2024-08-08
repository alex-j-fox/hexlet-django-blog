# from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View

from hexlet_django_blog.article.forms import ArticleForm
from hexlet_django_blog.article.models import Article

# from django.http import Http404

title = 'Список статей'


def index(request, tags: str = None, article_id: int = None):
    current_article = title
    if tags and article_id:
        current_article = f'Статья номер {article_id}. Тег {tags}'
    return render(request, 'index.html', context={'title': current_article})


class IndexView(View):
    template_name = 'articles/index.html'

    # def get(self, request, tags: str = '', article_id: int = None):
    def get(self, request, *args, **kwargs):
        current_article = title
        articles = Article.objects.all()[0:15]

        tags = kwargs.get('tags')
        article_id = kwargs.get('article_id')
        if tags and article_id:
            current_article = f'Статья номер {article_id}. Тег {tags}.'
        return render(request, self.template_name,
                      context={'title': current_article, 'articles': articles})


class ArticleView(View):
    template_name = 'articles/article.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, self.template_name,
                      context={'article': article})


class ArticleCreateView(View):
    template_name = 'articles/create.html'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    # self.fields['cat'].empty_label = 'Категория не выбрана'

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        mess = messages.get_messages(request)
        return render(request, self.template_name,
                      {'form': form, 'messages': mess})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Статья успешно создана')
            return redirect(reverse('articles_index'))
        else:
            messages.add_message(request, messages.ERROR, 'Статья не создана')
            return render(request, self.template_name, {'form': form})


class ArticleUpdateView(View):
    template_name = 'articles/update.html'

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('article_id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, self.template_name,
                      {'form': form, 'article': article})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('article_id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles_index'))
        else:
            return render(request, self.template_name, {'form': form})
