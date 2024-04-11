from django.urls import path
from .views import (
    login_view, register_view, logout_view
)

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
]
