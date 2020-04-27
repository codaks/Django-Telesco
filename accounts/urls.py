from . import views
from django.urls import include,path


urlpatterns = [
    path('register', views.register,name = "register"),
    path('login', views.login,name = "login"),
]
