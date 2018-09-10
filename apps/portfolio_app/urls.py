from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^bio$', views.bio, name="bio"),
    url(r'^projects$', views.projects, name="projects"),
    url(r'^hobbies$', views.hobbies, name="hobbies"),
    url(r'^travel$', views.travel, name="travel"),
]