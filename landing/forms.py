from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class TemplateForm(forms.Form):
    my_name = forms.CharField()
    # widget тоже нужен только для отображения в HTML
    my_email = forms.EmailField()
    my_subject = forms.CharField()
    my_message = forms.CharField(widget=forms.Textarea)


