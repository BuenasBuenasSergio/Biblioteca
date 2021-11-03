from django.db import models


class Genre(models.Model):
    name = models.CharField("Genero", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

class Author(models.Model):
    first_name = models.CharField("Nombre", max_length=100)
    last_name = models.CharField("Apellido", max_length=100)
    date_of_birth = models.DateField("Fecha nacimiento", null=True, blank=True)
    date_of_death = models.DateField("Fallecido", null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Book(models.Model):
    '''Libro de aplicacion de biblioteca...'''
    title = models.CharField(max_length=250)
    summary = models.TextField(blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    fecha = models.DateField(auto_now=True, null=True, help_text='Fecha de publicacion')
    #relaciones de autor y genero
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def muestra_genero(self):
        '''Muestra genero para admin'''
        return ', '.join([gen.name for gen in self.genre.all()[:3]])
    muestra_genero.short_description = 'Genero'

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'