# Importar pandas
import pandas as pd

# Meter el .json en DataFrame
df = pd.read_json('datos_pelis_plus.json')

# Seleccionar los datos del .json a convertir
datos = 'img url titulo year duracion'.split()

# Meter los datos en el array
df = df[datos]

# Convertir .json a .csv
df.to_csv("peliculas.csv", index=False)