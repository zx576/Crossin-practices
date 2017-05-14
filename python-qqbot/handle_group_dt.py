#-*- coding:utf-8 -*-

import sqlite3


class Group_dt():

    def __init__(self,groupname):

        self.groupname = groupname
        self.conn = ''
        self.build_or_connect(self.groupname)
        self.all_members = []
        self.extract_all_members()


    def __str__(self):
        return str(self.all_members)

    def build_or_connect(self,groupname):

        self.conn = sqlite3.connect('qqrobot.db')

        sql = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{0}';".format(groupname)
        res = self.conn.execute(sql).fetchone()[0]
        print(res)
        if res == 1:
            pass
        elif res == 0:
            sql_build = r'''
                CREATE TABLE {0}
                (
                    ID       INTEGER PRIMARY KEY,
                    NAME     TEXT
                );
                '''.format(groupname)
            print(sql_build)
            self.conn.execute(sql_build)


        else:
            print('error')

    def save(self,members_list):
        for member in members_list:
            sql = r'''
                    INSERT INTO {0}(ID,NAME)
                    VALUES(NULL,'{1}')
                   '''.format(self.groupname,member)

            self.conn.execute(sql)
        self.conn.commit()


    def extract_all_members(self):
        self.all_members = []
        sql = 'SELECT NAME FROM {0} '.format(self.groupname)
        # print(sql)
        query = self.conn.execute(sql)
        for i in query:
            self.all_members.append(i[0])

    def update(self,members_list):

        new_members = []
        for member in members_list:

            if member.__str__() in self.all_members:

                continue
            else:

                new_members.append(member)

        self.save(new_members)
        self.extract_all_members()
        return new_members
