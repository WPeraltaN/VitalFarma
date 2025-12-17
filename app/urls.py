from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('app.routes.main')),
    
    # RUTA PARA SOLICITAR EL RECETEO DE LA CONTRASENA
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name = "auth/password_reset_email.html",
        email_template_name = "auth/password_reset_email.html",
        subject_template_name = "auth/password_reset_subject.txt",
        success_url = "/password-reset/done/"
    ),name = "password_reset"),
    
    # RUTA PARA CUANDO SE SOLICITE CAMBIAR LA CONTRASENA
    path("password-reset/done/", auth_views.PasswordResetView.as_view(
        template_name = "auth/password_reset_done.html",
    ),name="password_reset_done"),
    
    # RUTA PARA CUANDO SE SOLICITE CAMBIAR LA CONTRASENA
    path("password-reset/<uid64>/<token>", auth_views.PasswordResetView.as_view(
        template_name = "auth/password_reset_confirm.html",
    ),name="password_reset_confirm"),
    
    path("password-reset/complete", auth_views.PasswordResetView.as_view(
        template_name = "auth/password_reset_complete.html",
    ),name="password_reset_complete"),
]
