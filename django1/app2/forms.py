from django import forms
from app2.models import students
class inputform(forms.ModelForm):
    class Meta:
        model=students
        fields=['name','college','course']