from django.conf.urls import url
from . import views
from . import final_algorithm1
"""from .views import index
from .views import index2
from .views import index3"""
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'sections/$', views.index2, name='index2'),
    url(r'sections/addAndDel/$',views.index3, name='index3'),
    url(r'sections/addAndDel/result$',final_algorithm1.result, name='getresult')
]