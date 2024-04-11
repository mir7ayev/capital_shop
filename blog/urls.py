from django.urls import path
from .views import (
    blog_view, blog_single,
)

urlpatterns = [
    path('', blog_view),
    path('<int:pk>/', blog_single),
]


