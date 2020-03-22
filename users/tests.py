# # users/test.py
# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse, resolve
#
# from users import views
# from users.forms import CustomUserCreationForm
# # Create your tests here.
#
#
# class CustomUserTest(TestCase):
#
#     def test_create_user(self):
#         main_user = get_user_model()
#         user = main_user.objects.create_user(username='dikku', email='barewa@gmail.com', password='kathmandu12317')
#         self.assertEqual(user.username, 'dikku')
#         self.assertEqual(user.email, 'barewa@gmail.com')
#         self.assertTrue(user.is_active)
#
#
# class SignupTest(TestCase):
#
#     def setUp(self):
#         url = reverse('signup')
#         self.response = self.client.get(url)
#
#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'users/signup.html')
#         self.assertContains(self.response, 'Signup')
#
#     def test_signup_form(self):  # new
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, CustomUserCreationForm)
#         self.assertContains(self.response, 'csrfmiddlewaretoken')
#
#     def test_signup_view(self):  # new
#         view = resolve('/accounts/signup/')
#
#         self.assertEqual(view.func.__name__, views.SignUpPageView.as_view().__name__)
#
#
#
