from .models import Task
from django.forms import ModelForm

class Todoform(ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']