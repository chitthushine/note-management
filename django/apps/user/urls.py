from django.urls import path

from .views import signup, login_view, custom_logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
]
