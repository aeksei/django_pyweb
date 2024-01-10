from django.contrib import admin

from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
