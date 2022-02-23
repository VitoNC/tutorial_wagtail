from django.db import models


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