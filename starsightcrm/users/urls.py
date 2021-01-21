from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
# namespace


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'
                                                                                 ), name='password_reset_complete'),

]
