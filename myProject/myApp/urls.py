from django.urls import path
from . import views


urlpatterns = [
    #url login
    path('', views.login_view, name='login'),
    #url home
    path('home/', views.home_view, name='home'),
    path('lichhoc/', views.lichhoc_view, name='lichhoc'),
    path('danhsach/', views.danhsach_view, name='danhsach'),
    path('tracuu/', views.tracuu_view, name='tracuu'),
    path('suadiem/', views.suadiem_view, name='suadiem'),    
    path('home/', views.home_view, name='home'), 
    path('Suadiem_btn/<int:id>/', views.Suadiem_btn_view, name='Suadiem_btn'),
    path('Xoadiem_btn/<int:id>/', views.Xoadiem_btn_view, name='Xoadiem_btn'),
    path('Nhapdiem/', views.Nhapdiem_view, name='Nhapdiem'),
     path('lich-hoc/', views.lich_hoc_list, name='lich_hoc_list'),  
    #url logout
    path('logout/', views.logout_view, name='logout'),
]
