from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_username = forms.CharField(label='username', max_length=100)
    your_email = forms.EmailField(label='email',max_length=100)
    your_password = forms.CharField(label='password',widget=forms.PasswordInput())


class LoginForm(forms.Form):
    nameoremail = forms.CharField(label='Your name or email', max_length=100)
    passlogin = forms.CharField(label='password',widget=forms.PasswordInput())