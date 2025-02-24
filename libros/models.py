from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.


## Modelo para libros

class Libro(models.Model):
    title = models.CharField('título', max_length=250)
    subtitle = models.CharField(max_length=40, blank=True)
    link = models.URLField()
    synopsis = models.CharField(max_length=1000, blank=True)
    rank = models.IntegerField()
    imagen = models.URLField()
    author = models.CharField(max_length=40, blank=True)
    urlAuthor = models.URLField()
    data = models.CharField(max_length=250, blank=True)
    price = models.CharField(max_length=30, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('link'),
        FieldPanel('rank'),
        FieldPanel('synopsis'),
        FieldPanel('imagen'),
        FieldPanel('data'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return f'{self.title} ({self.price})'


# Modelo de página de libros
class LibrosIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, libros, *args):
        page = request.GET.get('page')

        paginator = Paginator(libros, 10)

        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages



    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        libros = self.paginate(request, Libro.objects.all().order_by('rank'))

        context['libros'] = libros

        return context
    
    subpage_types = []
