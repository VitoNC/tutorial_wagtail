from email.mime import image
from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet



from wagtail.search import index

class NoticiasIndexPage(Page):
    introduccion = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        noticiaspages = self.get_children().live().order_by('-first_published_at')
        context['noticiaspages'] = noticiaspages
        
        return context

class NoticiasPage(Page):
    date = models.DateField("Fecha Noticia")
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)
    portada = models.ImageField()


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('portada'),

        MultiFieldPanel([
            FieldPanel('date'),
            ],
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', 
            label="Galería de imágenes"),
    ]

class NoticiasPageGalleryImage(Orderable):
    page = ParentalKey(NoticiasPage, 
        on_delete=models.CASCADE, 
        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]