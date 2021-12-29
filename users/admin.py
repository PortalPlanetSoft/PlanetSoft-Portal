from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'is_admin',
                    'is_editor',
                    'is_employee'
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)

# admin.site.register(Admin)
# admin.site.register(Editor)
# admin.site.register(Employee)
