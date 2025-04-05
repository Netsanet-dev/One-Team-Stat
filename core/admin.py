from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role']
    fieldsets = UserAdmin.fieldsets + (
    ('Role Info', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
    ('Role Info', {'fields': ('role',)}),
    )
    search_fields = ('username', 'email', 'role')
    list_filter = ('role', 'is_staff', 'is_active')
