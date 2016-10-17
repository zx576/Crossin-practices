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
                TITLE TEXT NOT NULL,
                YEAR  INT NOT NULL,
                COUNTRY TEXT,
                BRIEF TEXT
                );
        '''
        conn.execute(sql)
        conn.commit()
    conn.close()
    print('the table has been generated')



def insert(conn,title,year,country,brief):
    sql = '''
            INSERT INTO movie(ID,TITLE,YEAR,COUNTRY,BRIEF )
            VALUES (NULL,'%s','%s','%s','%s');
    '''%(title,year,country,brief)

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
        title = input('the movie\'s title:')
        year = input('the movie\'s year:')
        country = input('the movie\'s country：')
        brief = input('introduction to the movie:')
        insert(conn,title,year,country,brief)
    elif choice == '2':
        show_all(conn)

    conn.close()

main()
