from django import forms
from .models import Habit

class HabitCreationForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'category', 'frequency', 'target_streak']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-3 rounded-xl bg-[#433D8B]/30 '
                         'border border-[#433D8B]/60 text-[#C8ACD6] '
                         'focus:ring-2 focus:ring-[#C8ACD6] focus:outline-none',
                'placeholder': 'Habit Title'
            }),

            'category': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-3 rounded-xl bg-[#433D8B]/30 '
                         'border border-[#433D8B]/60 text-[#C8ACD6] '
                         'focus:ring-2 focus:ring-[#C8ACD6] focus:outline-none',
                'placeholder': 'Category'
            }),

            'frequency': forms.Select(attrs={
                'class': 'block w-full px-4 py-3 rounded-xl bg-[#433D8B]/30 '
                         'border border-[#433D8B]/60 text-[#C8ACD6] '
                         'focus:ring-2 focus:ring-[#C8ACD6] focus:outline-none'
            }),

            'target_streak': forms.NumberInput(attrs={
                'class': 'block w-full px-4 py-3 rounded-xl bg-[#433D8B]/30 '
                         'border border-[#433D8B]/60 text-[#C8ACD6] '
                         'focus:ring-2 focus:ring-[#C8ACD6] focus:outline-none',
                'placeholder': 'Target streak (# days)'
            }),
        }
