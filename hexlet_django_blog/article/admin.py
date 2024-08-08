from django.contrib import admin  # noqa

# Register your models here.
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_display = ('title', 'created_at')
    list_filter = ('created_at', 'updated_at')


# admin.site.register(Article, ArticleAdmin)
