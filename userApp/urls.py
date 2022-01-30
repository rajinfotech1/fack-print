from django.urls import path, include
from .views import register_request, login_request, logout_request

app_name = "userApp"   


urlpatterns = [
    # path("", homepage, name="homepage"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name= "logout"),
]
