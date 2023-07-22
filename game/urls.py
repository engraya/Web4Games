from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('main', views.main, name='main'),

    path('pongGame', views.pongGame, name='pongGame'),
    path('snakeGame', views.snakeGame, name='snakeGame'),
    path('tictactoeGame', views.tictactoeGame, name='tictactoeGame'),
    path('wordScrambleGame', views.wordScrambleGame, name='wordScrambleGame'),
    path('signIn', views.signIn, name="login"),
    path('signUp', views.signUp, name="register"),
    path('signOut', views.signOut, name="logout"),


    #password Reset urls
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="network/passwordManage/password_reset_form.html"), name="reset_password"),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name="network/passwordManage/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="network/passwordManage/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="network/passwordManage/password_reset_complete.html"), name="password_reset_complete")
]
