"""Programa para practicar web scraping, checando el precio de algun producto
para buscar ofertas"""

from bs4 import BeautifulSoup
import httplib2

def soup_web(link):
    http = httplib2.Http()
    response,content = http.request(link)
    soup = BeautifulSoup(content,"lxml")
    if soup:
        return soup
    else: print("\nNo hay pagina para analizar\n")

def product_title(soup):
    title = ""
    for id in soup.find_all('h1',attrs={'class':'ui-pdp-title'}):
        if id:
            title = id.text
    return f'{title}'

def product_price(soup):
    price = ""
    for id in soup.find_all('span',attrs={'class':'andes-money-amount__fraction'}):
        if id:
            price = id.text
    return f'{price}'

if __name__ == "__main__":
    # link = input("\nIngrese el link del articulo de mercado libre:\n")
    link = "https://articulo.mercadolibre.com.mx/MLM-1339765557-jabra-elite-3-navy-_JM#is_advertising=true&position=1&search_layout=stack&type=pad&tracking_id=0025254e-f336-481b-a0a5-f0fb5ac3aa19&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=YWRhYTJhMDItYzczMS00NDA2LTlhMTAtNGYxYmQwOGZjZWVk"
    if link != "":
        soup = soup_web(link)

        name = product_title(soup)
        price = product_price(soup)

        print(f'\n{name}\n{price}')
    
    else: print("\nLink incorrecto")

"""Conclusiones: Valores random en el precio, tecnicas de anti-scraping que utilizan las paginas web
para evitar el trafico de datos :("""