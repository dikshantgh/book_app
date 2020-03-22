# users/forms.py
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

"""We’re also not using CustomUserCreationForm anymore, but instead, that provided
by django-allauth"""
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         """The password field is implicitly included by default
#         and so does not need to be explicitly named here as well. Except for these I need to add all other fields"""
#         model = get_user_model()
#         fields = ('email', 'username',)
#
#
# class CustomUserChangeForm(UserChangeForm):
#     """It has three fields: username (from the user model), password1, and password2. It verifies that password1
#     and password2 match, validates the password using validate_password(), and sets the user’s password using
#     set_password()."""
#
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'username',)
#

"""Other fields for AbstractUser i.e get_user_model()username, email, is_staff, is_active, is_superuser,
last_login, and date_joined"""
