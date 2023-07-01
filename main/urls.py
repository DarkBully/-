from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('registration/', include('users.urls')),
    path('usercomment/', include('userscomments.urls'))
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

