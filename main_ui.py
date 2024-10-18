import making_request as m
import queries as q
from book_class import Book



def main():
    url = take_input()
    request = m.make_web(url)
    organized_scraped = m.soup_organize(request)
    needed_records = m.extract_records(organized_scraped)
    needed_links = m.extract_book_links(needed_records)
    for link in needed_links:
        request = m.make_request(link)
        organized_soup = m.soup_organize(request)
        info_soup = m.find_main_info(organized_soup)
        location_soup = m.find_location_info(organized_soup)
        my_book = Book(info_soup[0], info_soup[1], info_soup[2], location_soup[0], location_soup[3], location_soup[1])
        q.updating_new_book(my_book)

def take_input():
    while True:
        url = input('Enter Orange Library URL for search results filtered by Books: ')
        if 'format_category%3A%' in url:
            return url

if __name__ == '__main__':
    main()