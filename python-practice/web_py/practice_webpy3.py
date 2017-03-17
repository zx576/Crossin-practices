import web


url = ('/','index')

movies = [
    {'title':'forestgump','year':1994},
    {'title':'Titanic','year':1997}
        ]

render = web.template.render('templates/')
class index():
    def GET(self):
        return render.test(movies)


if __name__ == '__main__':
    app = web.application(url,globals())
    app.run()
