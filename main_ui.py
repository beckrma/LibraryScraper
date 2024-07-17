import making_request as m
from book_class import Book



def main():
    url = input('Enter Orange Library URL Ending with "Record": ')
    request = m.make_request(url)
    organized_scraped = m.soup_organize(request)
    info_soup = m.find_main_info(organized_scraped)
    location_soup = m.find_location_info(organized_scraped)
    my_book = Book(info_soup[0], info_soup[1], info_soup[5])
    title = my_book.get_title()
    print(title)






if __name__ == '__main__':
    main()