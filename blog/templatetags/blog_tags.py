from blog.models import BlogCategory as Category
from noticias.models import Noticias as Noticia

from django.template import Library

register = Library()


@register.inclusion_tag('components/categories_list.html', takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'categories': categories
    }

@register.inclusion_tag('components/noticias.html', takes_context=True)
def noticias_list(context):
    noticias = Noticia.objects.all()
    return {
        'request': context['request'],
        'noticias': noticias
    }