from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='portal/homepage.html', redirect_authenticated_user=True,
                                          redirect_field_name=None, success_url='employees/'), name='login'),

    path('logout/',
         login_required(auth_views.LogoutView.as_view(template_name='users/authentication/logged_out.html')),
         name='logout'),

    path('employees/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'praksaPlanetSoft.views.error_500'
handler404 = 'praksaPlanetSoft.views.error_404'
handler403 = 'praksaPlanetSoft.views.error_403'
handler400 = 'praksaPlanetSoft.views.error_400'
