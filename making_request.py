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
    pre_pre_title = texts.find('div', role='main')
    pre_title = pre_pre_title.find('div', class_='col-xs-12')
    title = pre_title.find('h1')
    actual_title = ''.join(title.find_all(text=True, recursive=False)).strip()
    specifics = texts.find('div', id='record-details-column')
    needs = specifics.find_all('div', class_='row')
    needed_information = []
    for lines in needs:
        needed_information.append(lines.find('div', class_='result-value'))
    extracted = extract_information(needed_information)
    extracted.insert(0, actual_title)
    return extracted

def find_location_info(soup_url: str):
    other = soup_url.find('div', id= 'more-details-accordion')
    copies = other.find('div', class_='accordion-inner')
    need = copies.find('table', class_='table table-striped')
    received = need.find_all('td')
    needed_text = []
    for lines in received:
        needed_text.append(lines.text)
    return needed_text

def extract_information(infos : list):
    extraction = []
    for info in infos:
        if not info:
            next
        else:
            extraction.append(info.text.strip())
    return extraction
