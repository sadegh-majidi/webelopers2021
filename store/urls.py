from django.contrib.auth.views import LoginView
from django.urls import path

from store.views import index, signup, signup_page

urlpatterns = [
    path('', index, name='home_page'),
    path('signup/', signup_page, name='signup_page'),
    path('signup/submit/', signup, name='signup'),
    path('login', LoginView.as_view(), name='login'),
]
