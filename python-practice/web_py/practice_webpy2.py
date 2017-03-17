import web

url = ('/','index')

movies = [
    {'title':'forestgump','year':1994},
    {'title':'Titanic','year':1997}
        ]


class indexs():
    def GET(self):
        page = ''
        for i in movies:
            page += '%s(%d)\n' %(i['title'],i['year'])
        return page


if __name__ == '__main__':
    app = web.application(url,globals())
    app.run()
