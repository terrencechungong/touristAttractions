from django.shortcuts import render, get_object_or_404, redirect
from .models import State, Attraction
from .forms import StateCreateForm, AttractionCreateForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def home(request):
  all_attractions = Attraction.objects.all()
  context = {"attractions": all_attractions, "name": request.user}
  return render(request, 'tourist_attractions/home.html', context)

def logout_view(request):
  logout(request)
  return redirect("home")


def loginn(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user != None:
      login(request, user)
      return redirect("home")
    else:
      return HttpResponse("Invalid Credentials")
  return render(request, "registration/login.html", context)


class Register(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/register.html"


def details(request, statename):
  attractions = Attraction.objects.all()
  context = {"attractions" : attractions, "statename" : statename.replace("-", " ")}
  return render(request, 'tourist_attractions/details.html', context)


class StateCreate(CreateView):
  model = State
  template_name = "tourist_attractions/state_create_form.html"
  form_class = StateCreateForm

class AttractionCreate(CreateView):
  model = Attraction
  template_name = "tourist_attractions/attraction_create_form.html"
  form_class = AttractionCreateForm

