from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')