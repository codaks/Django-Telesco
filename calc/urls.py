from . import views
from django.urls import include,path


urlpatterns = [
    path('', views.home,name = "home"),
    path('add', views.add,name = "add"),
]
