from django import forms
from .models import to_do


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = to_do
        fields = ['task', 'date']
