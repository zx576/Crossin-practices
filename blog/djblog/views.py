from django.shortcuts import render,redirect,render_to_response
from djblog.models import Article,Category,Comment
from django import forms
from django.contrib.auth import authenticate,models,login,logout
from django.http import HttpResponseRedirect
import urllib.request
import json

def log_in(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)#返回一个user-object
        print(user)
        if user and user.is_active:
            login(request,user)
            return HttpResponseRedirect('/blog/')
    return redirect('/blog')
def log_out(request):
    logout(request)
    return redirect('/blog')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print('a')
        errors = ''
        namecheck = models.User.objects.filter(username=username)
        #判断用户是否存在
        if len(namecheck) == 0 :
            #检查密码是否重复
            if password1 == password2:
                models.User.objects.create_user(
                    username=username,
                    password=password1
                )
                newuser = authenticate(username=username, password=password1)
                login(request, newuser)
                print('b')
                return redirect('/blog/')
            else:
                errors = '密码不相同'
                return render(request,'djblog/register.html',{'errors':errors})
        else:
            errors = '用户名已存在'
            return render(request, 'djblog/register.html', {'errors': errors})
    else:
        return render(request,'djblog/register.html')

def index(request):
    article_list = Article.objects.all()
    category_list = Category.objects.all()

    content = {'article_list':article_list,
               'category_list':category_list,
               }
    return render(request,'djblog/index.html',content)

def article(request,article_id):
    article_info = Article.objects.get(id=article_id)
    try:
        request.POST['likes']
        article_info.likes += 1
        article_info.save()
    except:
        pass
    else:
        return render(request, 'djblog/article.html', {'article': article_info})
        #return redirect('/blog/article/%s' % article_id)
    article_info.views += 1
    article_info.save()
    #print(article_info.title)
    return render(request,'djblog/article.html',{'article':article_info})

def cat(request,category_id):
    print(category_id)
    category_info = Category.objects.get(id=category_id)
    #article_list = Category.article_set.all
    content = {'category_info':category_info}
    return render(request,'djblog/cat.html',content)


def comments(request):
    if request.method == 'POST':
        '''print(request.POST)
        print(request.POST.get("id"))
        print(type(request.POST.get("comment")))'''
        content = request.POST.get('comment')
        id = request.POST.get('id')
        #print(id)
        #ar = request.POST.get('ar')[0]
        #print(request.POST)
        #print(content)
        Comment.objects.create(
            article_id = id,
            comments = content,
            articleid = id
            #article = ar
        )
        return redirect('/blog/article/%s'%(id))
    else:
        return redirect('/blog/')

def api(request):
    if request.method == 'POST':
        id = request.POST.get('idnum')
        ID_url = 'http://apis.baidu.com/chazhao/idcard/idcard?idcard='
        rep = urllib.request.Request(ID_url + id, headers={'apikey': '2fd858449606c0d8eaaea2cea84b14c7'})
        resp = urllib.request.urlopen(rep)
        content = resp.read().decode('utf-8')
        data = json.loads(content)
        info = data.get('data')
        content = {'info': info}
        return render(request,'djblog/api.html',content)
    else:
        pass

def userinfo(request,a):
    print(a)
    userinfom = models.User.objects.filter(id=a)
    content = {'user':userinfom}
    return render(request,'djblog/user.html',content)


####废弃代码片段
'''class IndexView(ListView):
    template_name = 'djblog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.all()#filter(status='p')
        for article in article_list:
            article.text = markdown2.markdown(article.text,)
        return article_list

    def get_context_data(self,**kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView,self).get_context_data(**kwargs)'''


'''class CategoryDetailView(DetailView):
    model = Category
    template_name = 'djblog/cat.html'
    pk_url_kwarg = 'category_id'
    context_object_name = 'category'''
'''def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        print(user_name)
        password = request.POST.get('password')
        try:
            idcheck = User.objects.get(username=user_name)
            if idcheck.password == password:
                return user_name
        except:
            print('not right username')
    else:
        return 0'''
'''class ArticleDetailView(DetailView):
    model = Article
    template_name = 'djblog/article.html'
    #context_object_name = 'article_detail'
    pk_url_kwarg = 'article_id'
    def get_object(self):
    obj = super(ArticleDetailView,self).get_object()
    obj.text = markdown2.markdown(obj.text)
    return obj'''
