# bookstore_project/urls.py
"""bookstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # # User management
    # path('accounts/', include('django.contrib.auth.urls')),    # new
    path('accounts/', include('allauth.urls')),    # new

    # Local apps
    # path('accounts/', include('users.urls')),    # new
    path('', include('pages.urls')),    # new
    path('books/', include('books.urls')),    # new



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # new


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),
    ]+ urlpatterns

"""to show the
files locally."""


"""Django’s auth app looks for templates within a templates/registration directory,
but django-allauth prefers they be located within a templates/account directory"""

"""We do
this by adding an account_ prefix so Django’s 'logout' will now be 'account_logout' ,
'login' will be 'account_login' , and signup will be account_signup ."""



"""We can
create any route we like but it’s common to use the same accounts/ one used by the
default auth app. Note that it’s important to include the path for users.urls below:
URL paths are loaded top-to-bottom so this ensures that any auth URL paths will be
loaded first."""


"""accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
https://docs.djangoproject.com/en/3.0/topics/auth/default/#module-django.contrib.auth.views
"""