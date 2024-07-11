class Book:
    def __init__(self, title : str, author : str, isbn : str):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.location = 'None'
        self.call_number = 0
        self.status = 'N/A'
