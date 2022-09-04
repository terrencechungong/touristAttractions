from django.urls import path, include

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("login/", views.login_view, name="login"),
  path("register/", views.Register.as_view(), name="register"),
  path("details/<statename>", views.details, name="details"),
  path("attraction/create", views.AttractionCreate.as_view(), name="attractioncreate"),
  path("state/create", views.StateCreate.as_view(), name="statecreate"),
  path("logout/", views.logout_view, name="logout")
]