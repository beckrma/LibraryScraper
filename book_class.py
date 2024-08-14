class Book:
    def __init__(self, title : str, author : str, isbn : str, location : str, status : str, callnum : str):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.location = location
        self.call_number = callnum
        self.status = status

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn