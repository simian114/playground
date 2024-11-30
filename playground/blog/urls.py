from django.urls import path
from .views import Front

app_name = 'blog'
urlpatterns = [
    path('', Front.as_view(), name='blog-front')
]
