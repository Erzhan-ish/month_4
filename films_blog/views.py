from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models
from django.views import generic

class SearchView(generic.ListView):
    template_name = 'show.html'
    context_object_name = 'film_list'
    paginate_by = 5

    def get_queryset(self):
        return models.FilmModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self,* ,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.FilmModel, id=id)
        context = {
            'film_id': film_id,
            }
        return render(request, template_name='show_detail.html', context=context)


def film_list_view(request):
    if request.method == 'GET':
        film_list = models.FilmModel.objects.all().order_by('-id')
        context = {
            'film_list': film_list
        }
        return render(request,template_name='show.html', context=context)



def about(request):
    if request.method == 'GET':
        return HttpResponse('Привет это мой первый проект на django')

def emoji(request):
    if request.method == 'GET':
        return HttpResponse('😆')

def image_proger_view(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://resizer.mail.ru/p/c4b1cb18-1b57-5a23-bd46-7eb1e60d167a/AQAKlf0JOSETi697'
                            'jlqZ2In4QCHOF8ApV7VVgy01SzGpOS3jUX8Cgk2Ki2C6670voZe4IAndYtFtZqJGfmm5xc0nP-Y.png" ')


