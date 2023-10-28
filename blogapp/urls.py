from django.urls import path
from .views import blog_view , blog_details

urlpatterns = [
    path('' , blog_view.as_view() , name = 'bloghome'),
    path('blog/<int:pk>/', blog_details.as_view(),name='blogdetails'),
]
