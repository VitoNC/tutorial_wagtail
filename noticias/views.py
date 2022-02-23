from django.shortcuts import render

from django.conf.urls import url


from django.views.generic import DetailView


from noticias.models import Noticia


# Create your views here.

def noticia_detail(request, title):

    noticia = Noticia.objects.get(title=title)
    context = {'object': noticia}
    return render(request, 'templates/noticias/noticia_detail.html', context)


class NoticiaDetailView(DetailView):
    model = Noticia



