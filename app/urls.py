from django.urls import path, include

urlpatterns = [
    path('', include('app.routes.main')),
]
