from django.contrib import admin
from .models import Student
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Student
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Course info',
            {
                'fields': (
                    'courses_cleared',
                )
            }
        )
    )

admin.site.register(Student, CustomUserAdmin)

