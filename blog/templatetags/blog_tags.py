from blog.models import BlogCategory as Category
from django.template import Library, loader

register = Library()


@register.inclusion_tag('components/categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'categories': categories
    }