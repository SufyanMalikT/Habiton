from .models import Habit, HabitCompletion
import datetime

def daily_streak_calculator(habit):
    completions = HabitCompletion.objects.filter(
        completed=True,
        habit=habit
    ).order_by('-date')

    streak = 0
    today = datetime.date.today()

    if not completions.exists():
        return 0

    latest_completion = completions[0].date

    if habit.frequency == 'daily':
        # streak only starts if last completion was today or yesterday
        if latest_completion not in (today, today - datetime.timedelta(days=1)):
            return 0
        
        # now count backwards
        for i, comp in enumerate(completions):
            expected_date = latest_completion - datetime.timedelta(days=i)
            if comp.date == expected_date:
                streak += 1
            else:
                break

    return streak

import datetime
from django.db.models import Q

def monthly_streak_calculator(habit):
    completions = HabitCompletion.objects.filter(
        habit=habit,
        completed=True,
        habit__frequency="monthly"
    ).order_by('-date')

    if not completions.exists():
        return 0

    streak = 0
    today = datetime.date.today()

    # Start from current month
    year = today.year
    month = today.month

    while True:
        # Calculate first and last day of this month
        month_start = datetime.date(year, month, 1)
        if month == 12:
            month_end = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            month_end = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

        # Check if ANY completion is inside that month
        has_completion = completions.filter(date__range=[month_start, month_end]).exists()

        if has_completion:
            streak += 1
        else:
            break

        # Move to previous month
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1

    return streak


import datetime

def weekly_streak_calculator(habit):
    completions = HabitCompletion.objects.filter(
        habit=habit,
        completed=True,
        habit__frequency='weekly'
    )

    if not completions.exists():
        return 0

    streak = 0
    today = datetime.date.today()

    # Get start of the current week (Monday)
    week_start = today - datetime.timedelta(days=today.weekday())
    week_end = week_start + datetime.timedelta(days=6)

    while True:
        # Check if any completion lies inside this week
        has_completion = completions.filter(date__range=[week_start, week_end]).exists()

        if not has_completion:
            break

        streak += 1

        # Move to previous week
        week_start -= datetime.timedelta(days=7)
        week_end -= datetime.timedelta(days=7)

    return streak


def streaks_calculator(habits):
    streaks = []
    for habit in habits:
        if habit.frequency == 'daily':
            data = {
                "habit": habit,
                "streak": daily_streak_calculator(habit)
            }
        elif habit.frequency == 'weekly':
            data = {
                "habit": habit,
                "streak": weekly_streak_calculator(habit)
            }
        elif habit.frequency == 'monthly':
            data = {
                "habit": habit,
                "streak": monthly_streak_calculator(habit)
            }
        streaks.append(data)
    return streaks



