from django.urls import path

from .views import homePage#, predictNews

urlpatterns = [
    path('home/', homePage, name='home-page'),
    # path('predictnews/', predictNews, name='predict-news'),
]