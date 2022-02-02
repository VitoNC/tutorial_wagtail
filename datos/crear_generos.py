
from pelis.models import Pelicula
import json
import os

# Lista de peliculas del json
if os.path.exists("datos/datos_pelis_plus.json"):
    pelis = json.load(open("datos/datos_pelis_plus.json"))
else:
    pelis = json.load(open("datos_pelis2.json"))

# Recorre datos del json