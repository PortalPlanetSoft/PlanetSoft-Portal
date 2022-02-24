"""praksaPlanetSoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='portal/templates/homepage.html',
                                          redirect_authenticated_user=True), name='login'),

    path('logout/',
         login_required(auth_views.LogoutView.as_view(template_name='portal/templates/authentication/logged_out.html')),
         name='logout'),

    path('password-change/',
         login_required(auth_views.PasswordChangeView.as_view(template_name='portal/templates/authentication'
                                                                            '/password_change.html')),
         name='password-change'),
    path('', include('portal.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'portal.views.error_500'
handler404 = 'portal.views.error_404'
handler403 = 'portal.views.error_403'
handler400 = 'portal.views.error_400'
