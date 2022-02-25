from sre_constants import CATEGORY
from unicodedata import category
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


class BlogIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        viajes = request.GET.get('viajes')
        qs = ''

        if viajes:
            entradas = self.subpage_types[ViajesPage]
            qs = f'categoria={viajes}'
        else:
            entradas = BlogIndexPage.objects.all()

        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['qs'] = qs

        return context

    parent_page_types = ['wagtailcore.Page']
    subpage_types = ['BlogPage', 'ViajesPage']



# Tags del Blog
class BlogTagIndexPage(Page):
    
    subpage_types = []
    
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )






# Modelo Página Blog
class BlogPage(Page):
    date = models.DateField("Fecha Post")
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ],
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', 
            label="Galería de imágenes"),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []


# Modelo Página Viajes
class ViajesPage(Page):
    lugar = models.CharField(max_length=30)
    date = models.DateField("Fecha Viaje", blank=True, null=True)
    intro = models.CharField("Introducción", max_length=250, blank=True, null=True)
    body = RichTextField(blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ],
            heading='Información'
        ),
        FieldPanel('lugar'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),

    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    



class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, 
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





@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categorías de blog'
        verbose_name = 'categoría de blog'



