from django.urls import path, include

from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('', include('allauth.urls')),
]
