from django.urls import path
from articles import views

urlpatterns =[
    path('articleslist', views.articlelist, name= 'articlelist')
]