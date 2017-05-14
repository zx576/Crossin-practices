import sqlite3
import os

def judge():
    path = os.path.exists('movies.db')
    conn = sqlite3.connect('movies.db')
    if not path:
        print('we\'re creating a table')
        sql = r'''
                CREATE TABLE movie
                (
                ID INTEGER PRIMARY KEY,
                identity TEXT,
                title TEXT NOT NULL,
                origin  TEXT NOT NULL,
                url TEXT,
                rating INT,
                image_url TEXT,
                directors TEXT,
                casts TEXT,
                year TEXT,
                genres TEXT,
                countries TEXT,
                summary TEXT
                );
        '''
        #identity,title,origin,url,rating,image_url,directors,casts,year,genres,countries,summary
        conn.execute(sql)
        conn.commit()
    conn.close()
    print('the table has been generated')



def insert(conn,id,title,origin,year,rating,directors,actors):
    sql = '''
            INSERT INTO movie(ids,title,origin,year,rating,directors,actors )
            VALUES ('%s','%s','%s','%s','%s','%s','%s');
    '''%(id,title,origin,year,rating,directors,actors)

    conn.execute(sql)
    conn.commit()
    conn.close()
    print('successfully insert')

def show_all(conn):
    sql = '''
        SELECT * FROM movie;
    '''
    all_info = conn.execute(sql)
    for i in all_info:
        print(i)

    print('all infomation has been print')

def main():
    judge()
    conn = sqlite3.connect('movies.db')
    print('1.插入，2.查看')
    choice = input('1 or 2')
    if choice == '1':
        id = input('the movie\'s id:')
        title = input('the movie\'s title:')
        origin = input('the movie\'s origin:')
        year = input('the movie\'s year:')
        rating = input('the movie\'s rating：')
        directors = input('the movie\'s directors::')
        actors = input('the movie\'s actors:')
        insert(conn,id,title,origin,year,rating,directors,actors)
    elif choice == '2':
        show_all(conn)

    conn.close()

main()
