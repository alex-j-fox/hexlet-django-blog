from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
