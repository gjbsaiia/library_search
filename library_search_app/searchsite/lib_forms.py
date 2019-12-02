from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length = 20)
