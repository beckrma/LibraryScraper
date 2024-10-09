import requests as r
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def make_request(url: str):
    current_request = r.get(url)
    return current_request

def make_web(url: str):
    chrome_options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(30)
    driver.get(url)
    html_re = driver.page_source
    driver.quit()
    return html_re

def soup_organize(request):
    try:
        soup = BeautifulSoup(request.content, 'html.parser') 
        return soup
    except AttributeError:
        soup = BeautifulSoup(request, 'html.parser')
        return soup

def extract_records(soup_url: str):
    records = []
    for num in range(1,21):
        if num%2 != 0:
            class_name = f"result record{num}"
            record = soup_url.find('div', class_= class_name)
            records.append(record)
        else:
            class_name = f"result alt record{num}"
            record = soup_url.find('div', class_= class_name)
            records.append(record)
    return records

def extract_book_links(record_list: list):
    link_list = []
    for records in record_list:
        links = records.find('a', class_= 'btn btn-xs btn-primary btn-wrap')
        if links is None:
            continue
        href_val = links['href']
        if len(href_val) == 0:
            continue
        link_list.append(f'https://copl.aspendiscovery.org/{href_val}')
    return link_list

def find_main_info(soup_url: str):
    texts = soup_url.find('div', id='main-content')
    pre_pre_title = texts.find('div', role='main')
    pre_title = pre_pre_title.find('div', class_='col-xs-12')
    title = pre_title.find('h1')
    actual_title = ''.join(title.find_all(text=True, recursive=False)).strip()
    author = soup_url.find('div', class_='result-value col-sm-8 col-xs-12')
    isbn = soup_url.find('div', text='ISBN')
    isbn_value = isbn.find_next_sibling('div', class_='result-value')
    needed_info = [author, isbn_value]
    extracted = extract_information(needed_info)
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
