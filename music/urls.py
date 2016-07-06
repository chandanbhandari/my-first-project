from django.conf.urls import url
from . import views

urlpatterns =[
    #/music/
    url('^$',views.index,name='index'),

    #music/712
    url(r'^(?p<album_id>[0-9]+)/$',views.detail,name='detail')
]
