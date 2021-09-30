from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from user_authentication import views as user_auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_profile.urls')),
    
    # AUTHENTICATION URLS
    path('sign-up/', user_auth_views.user_sign_up, name="register"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="user_authentication/user_sign_in.html"), name="login"),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="user_authentication/user_sign_out.html"), name="logout"),

    # REST FRAMEWORK URLS
    path('api/', include('user_profile.api.urls')), 
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
