#-*- coding:utf-8 -*-
import sqlite3
import os
DATABASE = 'address_list.db'

created = os.path.exists(DATABASE)
conn = sqlite3.connect(DATABASE)
if not created:
     conn.execute('''
        CREATE TABLE ADDRESSLIST
        (
            ID INTEGER PRIMARY KEY,
            NAME CHAR(8) NOT NULL,
            PHONE CHAR(16),
            EMAIL CHAR(64)
        );
        ''')
     print('end')


def insert(db,name,phonenum,email):
    sql = r'''
        INSERT INTO ADDRESSLIST(ID,NAME,PHONE,EMAIL)
        VALUES (NULL,'%s','%s','%s');
    '''%(name,phonenum,email)
    db.execute(sql)
    db.commit()
    print('success')

def search(db,keyword):
    sql = r'''
            SELECT * FROM ADDRESSLIST WHERE
            NAME LIKE '%%%s%%' or
            PHONE LIKE '%%%s%%' or
            EMAIL LIKE '%%%s%%';
          '''%(keyword,keyword,keyword)
    query = db.execute(sql)
    for q in query:
        print(q[0],'\t'.join(q[1:]))


def delete(db,cid):
    sql = r'SELECT * FROM ADDRESSLIST WHERE ID = %s;' %(cid)
    query = db.execute(sql)
    for q in query:
        print(q[0],'\t'.join(q[1:]))
    confirm = input('are u sure delete?[y/n]')
    if confirm.lower() == 'y':
        sql = r'DELETE FROM ADDRESSLIST WHERE ID=%s;'%cid
        query = db.execute(sql)
        db.commit()
        print('success')

def showall(db):
    sql = r'SELECT * FROM ADDRESSLIST'
    query = db.execute(sql)
    for q in query:
        print(q)
        #print(q[0],'\t'.join(q[1:]))

while True:
    choice = input('请选择：1.录入 2.查找 3.全部显示 4.删除 （回车退出）\n')
    if choice == '1':
        name = ''
        while name.strip() == '':
            name = input('姓名：')
        phonenum = input('手机号码：')
        email = input('邮箱：')
        insert(conn,name,phonenum,email)
    elif choice == '2':
        keyword = ''
        while keyword.strip() == '':
            keyword = input('查询关键字：')
        search(conn,keyword)

    elif choice == '3':
        showall(conn)

    elif choice == '4':
        cid = ''
        while not cid.isdigit():
            cid = input('联系人:')
        delete(conn,cid)
    elif choice == '':
        conn.close()
        break
    print()






