from django.shortcuts import render
from .models import blog
from django.views.generic import ListView , DetailView

# Create your views here.

class blog_view(ListView):
    model = blog
    template_name = 'bloghome.html'

class blog_details(DetailView):
    model = blog
    template_name = 'blogdetails.html'