import making_request as m




def main():
    url = input('Enter Orange Library URL Ending with "Record"')
    request = m.make_request(url)
    organized_scraped = m.soup_organize(request)
    info_list = m.find_main_info(organized_scraped)
    location_soup = m.find_location_info(organized_scraped)
    





if __name__ == '__main__':
    main()