import making_request as m
import queries as q
from book_class import Book



def main():
    url = take_input() # replace with page link
    request, driver = m.make_request(url)
    organized_scraped = m.soup_organize(request)
    needed_records = m.extract_records(organized_scraped)
    print(needed_records)
    driver.quit()
    
    '''
    info_soup = m.find_main_info(organized_scraped)
    location_soup = m.find_location_info(organized_scraped)
    my_book = Book(info_soup[0], info_soup[1], info_soup[5], location_soup[0], location_soup[3], location_soup[1])
    q.updating_new_book(my_book)
    '''


def take_input():
    url = input('Enter Orange Library URL Ending with "Record": ')
    return url



if __name__ == '__main__':
    main()