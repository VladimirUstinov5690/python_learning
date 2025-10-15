from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser


# Cпециальная форма из Django
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


# Это не связанная с моделью форма, поэтому берётся обычный forms.Form (чистая форма, без модели)
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


User = get_user_model()


# Тут мы работаем с моделью пользователя
class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'photo', 'password']
