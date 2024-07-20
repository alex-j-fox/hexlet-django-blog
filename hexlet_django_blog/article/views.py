# from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

title = 'Список статей!'


# def index(request):
# return HttpResponse('<h2>article</h2>')
# return render(request, 'articles.html', context={'title': title})

class IndexView(View):
    def get(self, request):
        return render(request, 'articles.html', context={'title': title})
