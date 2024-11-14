from django.urls import path
from . import views


urlpatterns = [
    #url login
    path('', views.login_view, name='login'),
    #url home
    path('home/', views.home_view, name='home'), 
    #url logout
    path('logout/', views.logout_view, name='logout'),
]
