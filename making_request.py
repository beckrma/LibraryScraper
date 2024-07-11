import requests as r
from bs4 import BeautifulSoup

def make_request(url: str):
    current_request = r.get(url)
    print(f'Request Code: {current_request}')
    return current_request  

def soup_organize(request):
    soup = BeautifulSoup(request.content, 'html.parser') 
    return soup

def find_main_info(soup_url: str):
    texts = soup_url.find('div', id= 'main-content')
    specifics = texts.find('div', id='record-details-column')
    needs = specifics.find_all('div', class_='row')
    needed_information = []
    for lines in needs:
        needed_information.append(lines.find('div', class_='result-value'))
    return needed_information

def find_location_info(soup_url: str):
    other = soup_url.find('div', id= 'more-details-accordion')
    copies = other.find('div', class_='accordion-inner')
    need = copies.find('table', class_='table table-striped')
    received = need.find_all('td')
    return received
