from django.shortcuts import render, redirect
from .models import Habit, HabitCompletion
from django.contrib.auth.decorators import login_required
import datetime
from .utils import streaks_calculator ,monthly_streak_calculator
from .forms import HabitCreationForm
# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'HabitonAPP_temps/home.html',{})

@login_required
def dashboard_view(request):

    habits = Habit.objects.filter(user=request.user)
    streaks = streaks_calculator(habits)
    habit_count = habits.count()
    todays_completions = HabitCompletion.objects.filter(habit__user=request.user,completed=True,date=datetime.date.today()).count()
    return render(request, 'HabitonAPP_temps/dashboard.html',{'habits':habits,'total_habits':habit_count,'todays_completions':todays_completions,'streaks':streaks})


def habits_list_view(request):
    habits = Habit.objects.filter(user = request.user)
    streaks = streaks_calculator(habits)
    return render(request,'HabitonAPP_temps/habits.html',{'habits':habits,'streaks':streaks})

def add_habit_view(request):
    if request.method == 'POST':
        form = HabitCreationForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habits_list")
    else:
        form = HabitCreationForm()
    return render(request, 'HabitonAPP_temps/habit_form.html',{'form':form})