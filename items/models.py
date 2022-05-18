from django.db import models


class Category(models.Model):
    parent = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)

    class Dtype(models.TextChoices):
        BOOK = "BOOK"
        ALBUM = "ALBUM"
        MOVIE = "MOVIE"

    dtype = models.CharField(max_length=16, choices=Dtype.choices, default=Dtype.BOOK)

    # Book
    artist = models.CharField(max_length=16, blank=True)
    etc = models.CharField(max_length=64, blank=True)

    # Album
    author = models.CharField(max_length=16, blank=True)
    isbn = models.CharField(max_length=32, blank=True)

    # Movie
    director = models.CharField(max_length=16, blank=True)
    actor = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name
