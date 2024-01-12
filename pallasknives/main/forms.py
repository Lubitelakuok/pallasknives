from .models import Task
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['first_name', 'last_name', 'email', 'blade_type', 'handle_type', 'color', 'message']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Адрес электронной почты',
            'blade_type': 'Тип клинка',
            'handle_type':'Тип рукояти',
            'color': 'Цвет',
            'message': 'Сообщение',
        }


