from django.shortcuts import render, get_object_or_404, redirect
from .models import State, Attraction
from .forms import StateCreateForm, AttractionCreateForm
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


#explain
@login_required(login_url="/login/")
def home(request):
  all_attractions = Attraction.objects.all()
  context = {"attractions": all_attractions, "name": request.user}
  return render(request, 'tourist_attractions/home.html', context)

def logout_view(request):
  logout(request)
  return redirect("home")

def login_view(request):
  username = request.POST.get('username')
  password = request.POST.get('password')

  user = authenticate(request, username=username, password=password)

  # Check if a user is verified and authenticated
  if user is not None:
    # Use the returned user object in login()
    login(request, user)

    # Redirect to home page after logging in
    return redirect("home")
  else:
    render(request, "registration/login.html")
  return render(request, "registration/login.html")

#explain
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

