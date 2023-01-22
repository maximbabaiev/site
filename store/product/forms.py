from django import forms


class LoginForm(forms.Form):
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
