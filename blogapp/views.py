from django.shortcuts import render
from .models import blog
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy

# listview and detailview is read in CRUD.
# Create your views here.

class blog_view(ListView):
    model = blog
    template_name = 'bloghome.html'

class blog_details(DetailView):
    model = blog
    template_name = 'blogdetails.html'

class blog_new(CreateView):
    model = blog
    template_name = 'blognew.html'
    fields = ['title' , 'author', 'body']

class blog_update(UpdateView):
    model = blog
    template_name = 'blogupdate.html'
    fields = ['title', 'body']

class blog_delete(DeleteView):
    model = blog
    template_name = 'blogdelete.html'
    success_url = reverse_lazy('bloghome')
