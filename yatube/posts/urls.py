from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='main_page'),
    path('group/<slug:any_slug>/', views.group_posts, name='group_list')
] 