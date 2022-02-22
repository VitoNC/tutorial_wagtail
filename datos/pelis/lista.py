from django.conf import settings

settings.configure(DEBUG=True)

from pelis.models import Pelicula

for p in Pelicula.objects.all():
    print(p)
    
