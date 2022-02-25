from django.db import models


from wagtail.core.models import Page

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


## Modelo para noticias 
@register_snippet # Registrado como snippet
class Noticia(models.Model):
    title = models.CharField('título', max_length=250)
    subtitle = models.CharField(blank=True, max_length=250)
    date = models.DateField()
    body = RichTextField(blank=True)
    imagen = models.URLField()


    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('imagen'),
    ]

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'noticias'
        verbose_name = 'noticia'



class NoticiasIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        noticias = Noticia.objects.all().order_by('-id')
        context['noticias'] = noticias
        return context

    subpage_types = []