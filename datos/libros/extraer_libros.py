'''
Programa que extrae los datos de https://www.imdb.com/chart/top/
y genera un json con los datos de las películas

Trabajo: 
* Inspeccionar la estructura de la web
* Extraer los datos de las películas con xpath
'''

from pydoc import synopsis
import requests
from lxml import html
from urllib.parse import urljoin
import json

headers = {"Accept-Language": "es-es,es;q=0.5"}



def detalle(url_libro):
    url = urljoin ('https://www.todostuslibros.com/libros', url_libro)
    
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


def datos_libro(libro):
    ''''
    Función que dado un elemento tr de imdb con 
    los datos de una película devuelve un diccionario
    con los datos de ...
    '''
    # datos a devolver
    datos = {}

    content = libro.xpath(".//div[@class='book-content']")
    action = libro.xpath(".//div[@class='book-action']")


    imagen = content.xpath(".//div[@class='book-image']")
    elementos = content.xpath(".//div[@class='book-details']")

    price = action.xpath(".//div[@class='book-price']")
    location = action.xpath(".//div[@class='book-location']")


    # url de la peli
    url = imagen.xpath(".//a/@href")[0]
    datos['url'] = url

    #imagen
    imagensrc = imagen.xpath(".//a/img/@src")[0]
    datos['img'] = imagensrc
    
    # rank
    rank = imagen.xpath(".//a/span/text()")[0]
    datos['rank'] = rank


    # titulo
    titulo = elementos.xpath(".//h2[@class='title']/text()")[0]
    datos['title'] = titulo

    # autor
    autor = elementos.xpath(".//h3[@class='author']/a/text()")[0]
    datos['author'] = autor

    # datosAutor
    urlAutor = elementos.xpath(".//h3[@class='author']/a/@href")[0]
    datos['urlAuthor'] = urlAutor

    # sinopsis
    sinopsis = elementos.xpath(".//p[@class='synopsis d-none']/text()")[0]
    datos['synopsis'] = sinopsis

    # editorial
    editorial = elementos.xpath(".//p[@class='data']/text()")[0]
    datos['editorial'] = editorial


    # precio
    precio = price.xpath(".//text()")[0]
    datos['price'] = precio

    # location
    compra = location.xpath(".//text()")[0]
    datos['location'] = compra


    datos.update(detalle(url))

    return datos

if __name__ == '__main__':

    url = 'https://www.todostuslibros.com/mas_vendidos'
    
    response = requests.get(url, headers=headers)
    pagina = html.fromstring(response.text)

    libros = pagina.xpath("//ul[@class='books']/li")

    # test
    #assert(len(libros) == 100)

    datos = [datos_libro(l) for l in libros]
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

