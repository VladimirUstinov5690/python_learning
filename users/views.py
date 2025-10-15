from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, LoginForm, ProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} успешно создан!')
            login(request, user)  # сразу авторизуем
            return redirect('home')
        else:
            print(form.errors)  # 🔍 для отладки
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            form.add_error(None, "Неверный email или пароль")
    return render(request, "users/login.html", {"form": form})


@login_required
def profile_view(request):
    user = request.user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            
            # Проверяем, изменён ли пароль
            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
                update_session_auth_hash(request,
                                         user)  # сохраняет сессию после смены пароля
            
            user.save()
            messages.success(request, 'Профиль успешно обновлён.')
            return redirect('profile')  # перезагружаем страницу
    else:
        form = ProfileForm(instance=user)
    
    return render(request, 'users/profile.html', {'form': form})


def logout_view(request):
    pass
