from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('fashion', views.fashion, name='fashion'),
    path('gifts', views.gifts, name='gifts'),
    path('ideas', views.ideas, name='ideas'),
    path('news', views.news, name='news'),
]