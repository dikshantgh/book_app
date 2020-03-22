# users/admin.py

# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
# from users.forms import CustomUserCreationForm, CustomUserChangeForm
# # from users.models import CustomUser
#
# Custom_User = get_user_model()
#
#
# class CustomUserAdmin(UserAdmin):
#     """the add_form is used when you construct a new CustomUser, whereas the simple form is used to
#     change data for an existing CustomerUser object."""
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = Custom_User
#     list_display = ['email', 'username', ]
#
#
# admin.site.register(Custom_User, CustomUserAdmin)
