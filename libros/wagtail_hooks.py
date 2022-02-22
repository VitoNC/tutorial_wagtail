from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from libros.models import Libro

class LibrosAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = Libro
    search_fields = ('title', 'cast', 'year')
    menu_icon = 'title' 
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)

modeladmin_register(LibrosAdmin)
