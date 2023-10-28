from django.urls import path
from .views import blog_view , blog_details , blog_new , blog_update , blog_delete

urlpatterns = [
    path('' , blog_view.as_view() , name = 'bloghome'),
    path('blog/<int:pk>/', blog_details.as_view(),name='blogdetails'),
    path('blog/new', blog_new.as_view(),name='blognew'),
    path('blog/<int:pk>/update/', blog_update.as_view(),name='blogupdate'),
    path('blog/<int:pk>/delete', blog_delete.as_view(),name='blogdelete')
]