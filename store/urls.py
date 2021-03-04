from django.urls import path

from store.views import index, signup_page, login_page, logout_user, contact_us_page, dashboard, create_new_product

urlpatterns = [
    path('', index, name='home_page'),
    path('signup/', signup_page, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', contact_us_page, name='contact_us'),
    path('dashboard/', dashboard, name='dashboard'),
    path('product/create/', create_new_product, name='create_new_product'),
]
