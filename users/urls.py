from django.urls import path, include

from .views import logout_view, login_view, registration_view


urlpatterns = [
    path('', registration_view, name='main'),
    path('logout', logout_view, name='logout'),
    path('login', login_view, name='login'),
    path('userpage/', include('user.urls'))
]