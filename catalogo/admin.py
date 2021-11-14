from django.contrib import admin
from django.db.models import fields

# Register your models here.
from .models import Author, Genre, Book, Language

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'muestra_genero']
    list_filter = ['author', 'genre', 'language']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    fieldsets = (
        ('Datos personales', 
        {'fields': ('first_name', 'last_name',)}), 
        ('Fechas', 
        {'fields': [('date_of_birth', 'date_of_death')]})
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
