import web
import sqlite3

urls = ('/','index','/movie/(\d+)','movie','/cast/(.*)','cast')

db = web.database(dbn='sqlite', db='movies.db')
render = web.template.render('templates/')
class index():
    def GET(self):
        movies = db.select('movie')
        print(movies)
        a = db.query('SELECT COUNT(*) AS COUNT FROM movie')
        print(a)
        b = a[0]
        print(b)
        count = b['COUNT']
        print(count)
        print(type(count))
        return render.test(movies,count,None)
    def POST(self):
        data = web.input()
        print(data)
        condition =  r'title like "%' + data.title + r'%"'
        search = db.select('movie',where=condition)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' +condition)[0]['COUNT']
        return render.test(search,count,data.title)

class movie():
    def GET(self,ID):
        id = int(ID)
        movies = db.select('movie',where='id=$id',vars=locals())[0]
        #print(movies)
        '''for i in movies:
            print(i)'''
        return render.movie(movies)

class cast():
    def GET(self,namestring):
        #print(namestring.encode('latin1'))
        namestring = namestring.encode('latin1').decode('utf8')
        print(namestring)
        condition = r'casts LIKE "%'+ namestring +r'%"'
        print(condition)
        movies = db.select('movie',where =condition )
        print(movies)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        print(count)
        return render.test(movies,count,namestring)

if __name__ == '__main__':
    app = web.application(urls,globals())
    app.run()