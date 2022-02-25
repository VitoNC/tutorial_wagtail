from blog.models import BlogCategory as Category
from noticias.models import Noticia

from django.template import Library

register = Library()


@register.inclusion_tag('components/categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'categories': categories
    }

@register.inclusion_tag('components/noticias_list.html',
                        takes_context=True)
def noticias_list(context):
    noticias = Noticia.objects.all().order_by('-id')[:5]

    return {
        'request': context['request'],
        'noticias': noticias,
    }