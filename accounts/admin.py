from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'phone_number', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-is_active',)
    list_display = ('email', 'phone_number', 'first_name', 'last_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )


admin.site.register(User, UserAdminConfig)
