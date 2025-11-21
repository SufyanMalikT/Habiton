from django.shortcuts import render, redirect
from .models import Habit, HabitCompletion
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'HabitonAPP_temps/home.html',{})
@login_required
def dashboard_view(request):
    habits = Habit.objects.filter(user=request.user)
    habit_count = habits.count()
    todays_completions = HabitCompletion.objects.filter(habit__user=request.user,completed=True,date=datetime.date.today()).count()
    return render(request, 'HabitonAPP_temps/dashboard.html',{'habits':habits,'total_habits':habit_count,'todays_completions':todays_completions})