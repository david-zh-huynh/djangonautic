from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url('', views.article_list, name="list"),
]

