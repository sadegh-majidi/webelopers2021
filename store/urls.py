from django.contrib.auth.views import LoginView
from django.urls import path

from store.views import index, signup, signup_page, login_page, login_user, logout_user

urlpatterns = [
    path('', index, name='home_page'),
    path('signup/', signup_page, name='signup_page'),
    path('signup/submit/', signup, name='signup'),
    path('login/', login_page, name='login_page'),
    path('login/submit/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
