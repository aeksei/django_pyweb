from django.urls import path

from . import views

app_name = "books_api"

urlpatterns = [
    path('books/<int:pk>/', views.BookAPIView.as_view(), name="book_detail"),
]
