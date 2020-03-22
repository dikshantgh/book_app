from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

# Create your tests here.
from pages import views
from pages.views import HomePageView


class HomePageTest(SimpleTestCase):

    def setUp(self):
        """Since the unit tests are executed top-to-bottom we can add a setUp method that will
        be run before every test."""

        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status(self):
        # response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_url_exists(self):
        # response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        # response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'pages/home.html')

    def test_home_page_contains_correct_string(self):
        # response = self.client.get('/')
        self.assertContains(self.response, 'Homepage')

    def test_home_page_resolves_homepageview(self):

        # The resolve() function can be used for resolving URL paths to the corresponding view functions.
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, 'pages/about.html')

    def test_about_page_contains(self):
        self.assertContains(self.response, 'This is the about section')

    def test_about_page_views(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, views.AboutPageView.as_view().__name__)

#
# class SignupTests(TestCase): # new
#     username = 'newuser'
#     email = 'newuser@email.com'
#
#     def setUp(self):
#         url = reverse('account_signup')
#         self.response = self.client.get(url)
#
#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'account/signup.html')
#         self.assertContains(self.response, 'Sign Up')
#         self.assertNotContains(
#         self.response, 'Hi there! I should not be on the page.')
#
#     def test_signup_form(self):
#         new_user = get_user_model().objects.create_user(
#         self.username, self.email)
#         self.assertEqual(get_user_model().objects.all().count(), 1)
#         self.assertEqual(get_user_model().objects.all()
#         [0].username, self.username)
#         self.assertEqual(get_user_model().objects.all()
#         [0].email, self.email)