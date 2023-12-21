from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('books/<int:book_id>/', views.book_detail, name="book_detail"),
    path('category/<slug:category_slug>/books/', views.category_books, name="category_detail_books")
]
