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

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, self.template_name,
                      {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if Article.objects.filter(title=obj.title).exists():
                messages.error(request,
                               'Статья с таким названием уже существует.',
                               extra_tags='alert alert-danger')
                return render(request, self.template_name, {'form': form})
            form.save()
            messages.success(request, 'Статья успешно создана')
            return redirect(reverse('articles_index'))
        else:
            messages.error(request, 'Статья не создана.',
                           extra_tags='alert alert-danger')
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
            obj = form.save(commit=False)
            if Article.objects.filter(title=obj.title).exclude(
                    pk=article_id).exists():
                messages.error(request,
                               'Статья с таким названием уже существует.',
                               extra_tags='alert alert-danger')
                return render(request, self.template_name,
                              {'form': form, 'article': article})
            form.save()
            messages.success(request, 'Статья успешно обновлена')
            return redirect(reverse('articles_index'))
        else:
            messages.error(request,
                           'Не удалось обновить статью.'
                           ' Проверьте правильность заполнения полей',
                           extra_tags='alert alert-danger')
            return render(request, self.template_name, {'form': form})
