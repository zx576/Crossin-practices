#-*- coding:utf-8 -*-

import sqlite3
import os
import json
import re


'''
封装操作编程教室所有教学资源的数据库方法


'''


class Resource_dt():

    def __init__(self):

        self.keywords_dict = {}
        self.conn = ''
        self.build_or_connect('qqrobot.db')
        self.extract_all_keywords()
        # print(self.keywords_dict)

    def build_or_connect(self, database_name):
        '''
        function:connect a existing sqlite3 database,build one if it doesn't exsits
        >>>build_or_connect('qqrobot.db')
        >>><sqlite3.Connection object at 0x0000000000818650>
        '''
        created = os.path.exists(database_name)
        self.conn = sqlite3.connect(database_name)

        if not created:
            self.conn.execute('''
                CREATE TABLE RESOURCE
                (
                    ID       INTEGER PRIMARY KEY,
                    TITLE    CHAR(100)  NOT NULL,
                    URL      TEXT,
                    KEYWORDS TEXT       NOT NULL,
                    CONTENT  TEXT,
                    STATUS   INTEGER    NOT NULL
                );
                ''')

    def extract_all_keywords(self):
        self.keywords_dict = {}
        sql = 'SELECT ID,KEYWORDS FROM RESOURCE'
        query = self.conn.execute(sql)
        # print(len(query))
        for item in query:
            if item[1] in self.keywords_dict.keys():
                self.keywords_dict[item[1]].append(item[0])
            else:
                self.keywords_dict[item[1]] = [item[0]]

    def insert_item(self, title, url, keywords, content):
        '''insert an item into sqlite3'''

        sql = r'''
                INSERT INTO RESOURCE(ID,TITLE,URL,KEYWORDS,CONTENT,STATUS)
                VALUES(NULL,"%s","%s","%s","%s",1)
               ''' % (title, url, keywords, content)

        self.conn.execute(sql)
        self.conn.commit()
        self.extract_all_keywords()

    def search_items(self, id, title, url, keywords, content):

        if id and id != 'none':
            sql = 'SELECT URL,CONTENT FROM RESOURCE WHERE ID = %s;' % id
            query = self.conn.execute(sql).fetchone()

            return query

        else:
            res_dict = self.searchf_items_for_group(keywords)
            return res_dict

    def search_items_for_group(self, content):

        res_id = []
        for key, value in self.keywords_dict.items():
            if content in key:
                for num in value:
                    res_id.append(num)

        result = {}
        for i in res_id:
            result['ele%d' % i] = {}
            sql = 'SELECT TITLE,URL,CONTENT FROM RESOURCE WHERE ID = %d;' % i
            query = self.conn.execute(sql).fetchone()
            result['ele%d' % i]['title'] = query[0]
            result['ele%d' % i]['url'] = query[1]
            result['ele%d' % i]['content'] = query[2]


        return result

    def update_items(self, id, title, url, keywords, content):

        sql = "UPDATE RESOURCE SET TITLE = '{0}' , URL = '{1}' , KEYWORDS = '{2}' , CONTENT = '{3}' WHERE ID = '{4}'".format(
            title, url, keywords, content, id)
        # print(sql)
        try:
            self.conn.execute(sql)
        except Exception as e:
            print(e)
            return '失败'
        else:
            return 'ok'

        self.extract_all_keywords()

    def extract_item_by_id(self, id):
        sql = 'SELECT TITLE FROM RESOURCE WHERE ID = {0}'.format(id)
        query = self.conn.execute(sql).fetchone()
        return query
