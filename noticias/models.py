from email.mime import image
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


from wagtail.search import index


@register_snippet
class Noticias(models.Model):
    titulo = models.CharField(max_length=30, blank=False)
    date = models.DateField("Fecha Noticia")
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)

    content_panels = [
        FieldPanel('titulo'),
        FieldPanel('portada'),

        MultiFieldPanel([
            FieldPanel('date'),
            ],
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'noticias'
        verbose_name = 'noticia'

    
'''
class NoticiasPageGalleryImage(Orderable):
    page = ParentalKey(Noticias, 
        on_delete=models.CASCADE, 
        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]'''