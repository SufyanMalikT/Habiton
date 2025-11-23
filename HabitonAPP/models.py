from django.db import models
from accounts.models import CustomUser
import datetime
# Create your models here.


class Habit(models.Model):
    class FrequencyChoices(models.TextChoices):
        DAILY = 'daily', 'Daily'
        WEEKLY = 'weekly', 'Weekly'
        MONTHLY = 'monthly', 'Monthly'
        
    user = models.ForeignKey(CustomUser,related_name='habits',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    frequency = models.CharField(max_length=10,choices=FrequencyChoices,default=FrequencyChoices.DAILY)
    target_streak = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.frequency})"
    
    def has_completed_today(self):
        return self.completions.filter(user=self.user,completed=True,date=datetime.date.today()).exists()

class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, related_name='completions',on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('habit','date')


    def __str__(self):
        return f"{self.habit.title} - {self.date} - {'Done' if self.completed else 'Pending'}"