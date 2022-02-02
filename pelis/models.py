from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from wagtail.snippets.models import register_snippet

# Create your models here.

## Page que mostrará el index de las películas
## Hereda solo de Home y no descendientes


# Modelo Género Pelicula
class Genre(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nombre
    panels = [
        FieldPanel('nombre')
    ]
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'



## Modelo para películas

class Pelicula(models.Model):
    title = models.CharField('título', max_length=250)
    slug = models.SlugField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    link = models.URLField()
    place = models.IntegerField()
    year = models.IntegerField()
    imagen = models.URLField()
    cast = models.CharField(max_length = 250, 
        help_text='Introduzca nombres separados por comas')
    generos = models.ManyToManyField(Genre)

    panels = [
        FieldPanel('title'),
        FieldPanel('rating'),
        FieldPanel('link'),
        FieldPanel('place'),
        FieldPanel('year'),
        FieldPanel('imagen'),
        FieldPanel('cast'),
        FieldPanel('generos')
    ]
    def __str__(self):
        return f'{self.title} ({self.year})'




class PelisIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]


    def get_pelis(self):
        return Pelicula.objects.all()


    def paginate(self, request):
        page = request.GET.get('page')
        decada = request.GET.get('decada')

        if decada:
            peliculas = Pelicula.objects.filter(year__gte=1990, year__lt=2000)
        else:
            peliculas = Pelicula.objects.all()

        paginator = Paginator(peliculas, 25)
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

        # BreadPage objects (get_breads) are passed through pagination
        pelis = self.paginate(request)

        context['peliculas'] = pelis

        
        return context
    
    






    