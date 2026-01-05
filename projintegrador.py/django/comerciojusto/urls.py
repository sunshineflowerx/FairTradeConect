from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('pos-login/', views.pos_login, name='pos_login'),
    path('area/produtor/', views.area_produtor, name='area_produtor'),
    path('area/empresa/', views.area_empresa, name='area_empresa'),
    path('area/gestor/', views.area_gestor, name='area_gestor'),
    path('area/operador/', views.area_operador, name='area_operador'),
]
