from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article,name='article'),
    url(r'^cat/(?P<category_id>\d+)',views.cat,name='cat'),
    url(r'^comment/',views.comments,name='comments'),
    url(r'^api/$',views.api,name='api'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.log_in,name='login'),
    url(r'^logout/$',views.log_out,name='logout'),
    url(r'^user/([0-9]+)$',views.userinfo,name='userinfo')
    #url(r'^register/success/$',views.success,name='success')

]



