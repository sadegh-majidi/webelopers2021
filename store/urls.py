from django.urls import path

from store.views import index, signup_page, login_page, logout_user

urlpatterns = [
    path('', index, name='home_page'),
    path('signup/', signup_page, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
]
