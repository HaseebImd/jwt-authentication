from django.urls import path
from .views import LoginView, RestrictedView, GetAdvice

urlpatterns = [
    path("api/login", LoginView.as_view(), name="login"),
    path("api/restricted", RestrictedView.as_view(), name="restricted"),
    path("api/get-advice", GetAdvice.as_view(), name="get-advice"),
]
