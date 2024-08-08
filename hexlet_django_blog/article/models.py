from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title
