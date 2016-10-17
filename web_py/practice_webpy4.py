import web
import sqlite3

urls = ('/','index','/movie/(\d+)','movie')

db = web.database(dbn='sqlite', db='movies.db')
print('s')
render = web.template.render('templates/')
class index():
    def GET(self):
        movies = db.select('movie')
        #for i in movies:
        #    print(i)
        return render.test(movies)
    def POST(self):
        data = web.input()
        condition =  r'title like "%' + data.title + r'%"'
        search = db.select('movie',where=condition)
        return render.test(search)



class movie():
    def GET(self,ID):
        print('a')
        id = int(ID)
        movies = db.select('movie',where='ID=$id',vars=locals())[0]
        print(movies)
        '''for i in movies:
            print(i)'''
        return render.movie(movies)


if __name__ == '__main__':
    app = web.application(urls,globals())
    app.run()