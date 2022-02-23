'''
crear libros

ejecutar:

python manage.py shell < datos/libros/crear_libros.py
'''

from libros.models import Libro
import json
import os


# borrar pelis
for l in Libro.objects.all():
    l.delete()

#lista de películas del json
if os.path.exists("datos/libros/datos_libros.json"):
    libros = json.load(open("datos/libros/datos_libros.json"))
else:
    libros = json.load(open("datos_libros.json"))


'''
{
        "img": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg",
        "url": "/title/tt0111161/",
        "cast": "Frank Darabont (dir.), Tim Robbins, Morgan Freeman",
        "titulo": "Cadena perpetua",
        "year": "1994"
    },
'''

for l1 in libros:
    l = Libro()
    l.title = l1["title"]
    l.subtitle = l1["subtitle"]
    l.author = l1["author"]
    l.urlAuthor = l1["urlAuthor"]
    l.link = l1["url"]
    l.rank = l1["rank"]
    l.synopsis = l1["synopsis"]

    l.imagen = l1["image"]

    l.data = l1["data"]
    l.price = l1["price"]

    l.save()