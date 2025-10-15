from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('username', 'photo')}),
        ('Права доступа', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('email', 'username')
