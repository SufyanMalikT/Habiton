from django.urls import path
from .views import dashboard_view, home_view,habits_list_view, add_habit_view
urlpatterns = [
    path('',home_view,name='home'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('habits/',habits_list_view,name='habits_list'),
    path('add_habit/',add_habit_view, name='add_habit')
]