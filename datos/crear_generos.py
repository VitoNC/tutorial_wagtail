'''
crear generos
ejecutar:
python manage.py shell < datos/crear_generos.py
'''

from pelis.models import Pelicula, Genre
from django.utils.text import slugify
import json
import os



#lista de películas del json
if os.path.exists("datos/datos_pelis2.json"):
    pelis = json.load(open("datos/datos_pelis2.json"))
else:
    pelis = json.load(open("datos_pelis2.json"))

# recorre datos del json
for p in pelis:
    slug = slugify(f'{p["titulo"]} ({p["year"]})')
    pelicula = Pelicula.objects.get(slug=slug)  # recupera película por su slug
    generos = p.get('genre')  # géneros de la película (lista en el json)
    for genero in generos:
        genobj, created = Genre.objects.get_or_create(nombre=genero) # Recupera o crea el género si no existe
        pelicula.generos.add(genobj) # añade la relación m2m