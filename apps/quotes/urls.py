from django.conf.urls import url
from . import views

app_name = 'quotes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^favorite$', views.favorite, name='favorite'),
    url(r'^remove$', views.remove, name='remove'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^deleteQuote$', views.deleteQuote, name='deleteQuote'),
]
