from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, RegisterView, LoginView

router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author')
router.register('book', BookViewSet, basename='book')
router.register('register', RegisterView, basename='register')
router.register('login', LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]