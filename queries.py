# File for making SQL queries and making main more clean
import psycopg2
from dotenv import load_dotenv
import os

def updating_new_book(my_book : object):
    title_b = my_book.get_title()
    author_b = my_book.get_author()
    isbn_b = my_book.get_isbn()
    load_dotenv()
    conn = psycopg2.connect(host=os.getenv("my_host"), dbname=os.getenv("my_dbname"), user=os.getenv("my_user"), password=os.getenv("my_password"), port=os.getenv("my_port"))
    curs = conn.cursor()
    query = '''INSERT INTO "Books"(title, author, isbn, location, status, callnum) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (isbn)
                    DO UPDATE SET
                      Location = EXCLUDED.Location,
                      Status = EXCLUDED.Status,
                      CallNum = EXCLUDED.CallNum;
                 '''    
    curs.execute(query, (title_b, author_b, isbn_b, my_book.location, my_book.status, my_book.call_number))
    conn.commit()
    curs.close()
    conn.close()