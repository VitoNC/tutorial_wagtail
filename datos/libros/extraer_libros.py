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



#def detalle(url_libro):
#    url = urljoin ('https://www.todostuslibros.com/libros', url_libro)
#    
#    response = requests.get(url, headers=headers)
#    pagina = html.fromstring(response.text)
#    script = pagina.xpath('//script[@type="application/ld+json"]')[0]
#    datos = json.loads(script.text)

    # parental
#    metadatos = pagina.xpath('//ul[contains(@class, "TitleBlockMetaData")]/li')

#    parental = metadatos[1].xpath('.//a[contains(@href, "parentalguide/certificates")]')[0].text
#    datos['parental'] = parental
    
#    duracion = metadatos[2].text_content()
#    datos['duracion'] = duracion

#    return datos


def datos_libro(libro):
    ''''
    Función que dado un elemento tr de imdb con 
    los datos de una película devuelve un diccionario
    con los datos de ...
    '''
    # datos a devolver
    datos = {}


    #Bien hecho A PARTIR DE AQUI

    elementos = libro.xpath(".//div")
    image = elementos[2]
    details = elementos[3]
    price = elementos[6]
    # location = elementos[7]

    url = image.xpath(".//a/@href")[0]
    datos['url'] = url

    rank = image.xpath(".//a/span/text()")[0].strip()
    datos['rank'] = rank

    imagen = image.xpath(".//a/img/@src")[0]
    datos['image'] = imagen


    # Titulo y Subtitulo
    title = details.xpath(".//h2[@class='title']/a/text()")[0].strip()
    datos['title'] = title

    subtitulos = details.xpath(".//h3[@class='subtitle']/a/text()")
    if subtitulos:
        subtitle = subtitulos[0].strip()
    else:
        subtitle = ''
    datos['subtitle'] = subtitle


    # Autor
    author = details.xpath(".//h3[@class='author']/a/text()")[0]
    datos['author'] = author

    urlAuthor = details.xpath(".//h3[@class='author']/a/@href")[0]
    datos['urlAuthor'] = urlAuthor


    # Sinopsis
    try:
        synopsis = details.xpath(".//p[@class='synopsis d-none d-md-block d-lg-block d-xl-block']/text()")[0]
    except IndexError:
        synopsis = ''
    

    datos['synopsis'] = synopsis

    # Editorial
    data = details.xpath(".//p[@class='data']/text()")[0]
    datos['data'] = data


    # Precio
    price = price.xpath(".//strong/text()")[0].strip()
    datos['price'] = price


    # Location
    # location = location.xpath(".//p/span/text()")[0]



    # datos.update(detalle(url))

    return datos

if __name__ == '__main__':

    url = 'https://www.todostuslibros.com/mas_vendidos?page={}'
    datos = []
    for x in range(1, 11):
    
        response = requests.get(url.format(x), headers=headers)
        pagina = html.fromstring(response.text)

        libros = pagina.xpath("//ul[@class='books']/li")

        # test
        #assert(len(libros) == 100)

        datos.extend([datos_libro(l) for l in libros])
    json.dump(datos, open('datos_libros.json', 'w'))



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

