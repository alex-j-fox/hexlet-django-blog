from django.shortcuts import render
# from django.urls import reverse
# from django.views.generic import View
from django.views.generic.base import TemplateView


# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World',
#     })


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

    def get(self, request, **kwargs):
        return render(request, 'index.html', context={'who': 'World'})
        # return redirect(
        #     reverse('article', kwargs={'tags': 'Python', 'article_id': 42}))


# class Error404View(View):
#     template_name = '404.html'

#     def get(self):
#         return render(self.request, '404.html')


def about(request):
    return render(request, 'about.html')
