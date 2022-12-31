from django.urls import path
from Myapp import views, Api
urlpatterns = [

    path('', views.dht11, name='Data'),

##api
path('api/list', Api.Dlist, name='DHT11List'),
# genericViews
path('api/post', Api.Dhtviews.as_view(), name='DHT_post'),



path('data2/', views.dht112, name='data2'),
path('data3/', views.dht113, name='data3'),
path('data4/', views.dht114, name='data4'),
    #data24H
path('data5/', views.dhttabjr1, name='data5'),
path('data6/', views.dhtgrajr1, name='data6'),
    #data48H
    path('data7/', views.data48, name='data7'),
    path('data8/', views.graph48, name='data8'),
    #data72H
    path('data9/', views.data72, name='data9'),
    path('dataa0/', views.graph72, name='data10'),


    ]

