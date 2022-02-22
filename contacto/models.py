from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


# Create your models here.

class Contacto(Page):
    descripcion = models.CharField(max_length=100)

    content_panels = Page.content_panels + [
        FieldPanel('descripcion'),
    ]

    parent_page_types = ['wagtailcore.Page']
    subpage_types = []

