from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from . import views

# app_name = "books_api"

router = SimpleRouter()
router.register("categories", views.CategoryViewSet)
...

urlpatterns = [
    path('books/<int:pk>/', views.BookAPIView.as_view(), name="book_detail"),
    path('books/', views.BookListCreateAPIView.as_view(), name="book_list"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', include(router.urls))
]
