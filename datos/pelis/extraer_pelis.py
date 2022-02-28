'''
Programa que extrae los datos de https://www.imdb.com/chart/top/
y genera un json con los datos de las películas

Trabajo: 
* Inspeccionar la estructura de la web
* Extraer los datos de las películas con xpath
'''

import requests
from lxml import html
from urllib.parse import urljoin
import json

headers = {"Accept-Language": "es-es,es;q=0.5"}



def detalle(url_peli):
    url = urljoin ('https://www.imdb.com', url_peli)
    
    response = requests.get(url, headers=headers)
    pagina = html.fromstring(response.text)
    script = pagina.xpath('//script[@type="application/ld+json"]')[0]
    datos = json.loads(script.text)

    # parental
    metadatos = pagina.xpath('//ul[contains(@class, "TitleBlockMetaData")]/li')

    parental = metadatos[1].xpath('.//a[contains(@href, "parentalguide/certificates")]')[0].text
    datos['parental'] = parental
    
    duracion = metadatos[2].text_content()
    datos['duracion'] = duracion

    return datos


def datos_peli(peli):
    ''''
    Función que dado un elemento tr de imdb con 
    los datos de una película devuelve un diccionario
    con los datos de ...
    '''
    # datos a devolver
    datos = {}

    elementos = peli.xpath(".//td")
    imagen = elementos[0]
    titulo = elementos[1]
    rating = elementos[2]




    #imagen
    imagensrc = imagen.xpath(".//img/@src")[0]
    datos['img'] = imagensrc

    # url de la peli
    url = titulo.xpath(".//a/@href")[0]
    datos['url'] = url



    # cast
    cast = titulo.xpath(".//a/@title")[0]
    datos['cast'] = cast

    # titulo
    titulo_ = titulo.xpath(".//a/text()")[0]
    datos['titulo'] = titulo_

    # año
    year = titulo.xpath(".//span/text()")[0].replace("(", "").replace(')', '')
    datos['year'] = year

    # ranking 
    pospunto = titulo.text_content().find('.')
    ranking = titulo.text_content()[:pospunto].strip()
    datos['ranking'] = ranking

    # rating 
    rating_ = rating.xpath(".//strong/text()")[0]
    datos['rating'] = rating_
    
    datos.update(detalle(url))

    return datos

if __name__ == '__main__':

    url = 'https://www.imdb.com/chart/top/'
    
    response = requests.get(url, headers=headers)
    pagina = html.fromstring(response.text)

    peliculas = pagina.xpath("//table[@data-caller-name='chart-top250movie']/tbody/tr")

    # test
    assert(len(peliculas) == 250)

    datos = [datos_peli(p) for p in peliculas]
    json.dump(datos, open('datos_pelis_plus.json', 'w'))



# Automatizar Autenticación en sitios Web


# sesion = requests.session()

#urllogin = 'http://localhost:8000/admin/login/'

#datos = {}
#datos['username'] = 'usuario'
#datos['password'] = 'contraseña'


#respuesta = sesion.get(url)

#doc = html.fromstring(respuesta.content)

#datos['csrfmiddlewaretoken'] = doc.xpath("//input[@name='csrfmiddlewaretoken']/value")

#resp = sesion.post(urllogin, data = datos)

