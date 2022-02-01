'''
crear películas

ejecutar:

python manage.py shell < datos/crear_peliculas.py
'''

from pelis.models import Pelicula
import json
import os


# borrar pelis
for p in Pelicula.objects.all():
    p.delete()

#lista de películas del json
if os.path.exists("datos/datos_pelis_plus.json"):
    pelis = json.load(open("datos/datos_pelis_plus.json"))
else:
    pelis = json.load(open("datos_pelis_plus.json"))


'''
{
        "img": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg",
        "url": "/title/tt0111161/",
        "cast": "Frank Darabont (dir.), Tim Robbins, Morgan Freeman",
        "titulo": "Cadena perpetua",
        "year": "1994"
    },
'''

for p1 in pelis:
    p = Pelicula()
    p.title = p1["titulo"]
    p.rating = p1["rating"].replace(',', '.')
    p.link = "https://www.imdb.com" + p1["url"]
    p.place = p1["ranking"]
    year = p1["year"]
    if year.isdigit():
        p.year = p1["year"]
    else:
        p.year = 0
    p.imagen = p1["img"]
    p.cast = p1['cast']
    p.save()
