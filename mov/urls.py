from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies.views import (
    home,
    movies_list,
    about_view,
    react_movie,
    rate_movie,
    comment_movie,
    contact_view,
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('collection/', movies_list, name='movies_list'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    # ✅ FIXED: React and Comment endpoints FIRST (before other movies paths)
    path('movies/react/', react_movie, name='react_movie'),
    path('movies/rate/', rate_movie, name='rate_movie'),
    path('movies/comment/', comment_movie, name='comment_movie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
