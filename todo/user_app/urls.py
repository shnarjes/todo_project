from django.urls import path, include
from user_app.views import login, register, logout

app_name = 'user_app'
urlpatterns = [
    path("", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),

]