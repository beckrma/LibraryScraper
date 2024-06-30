import requests as r
from bs4 import BeautifulSoup

def make_request(url: str):
    current_request = r.get(url)
    #print(f'Request Code: {current_request}')
    return current_request  

def soup_organize(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    #print(soup.prettify()) 
    return soup


if __name__ == '__main__':
    url = make_request('https://copl.aspendiscovery.org/Record/a370813')
    my_soup = soup_organize(url)
    texts = my_soup.find('div', id= 'main-content')
    specifics = texts.find('div', id='record-details-column')
    needs = specifics.find_all('div', class_='row')
    needed_information = []
    for lines in needs:
        needed_information.append(lines.find('div', class_='result-value'))
    
    for info in needed_information:
        if(not info):
            next
        else:
            print(info.text.strip())

    