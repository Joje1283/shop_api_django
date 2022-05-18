from django.db import models


class Category(models.Model):
    parent_id = models.ForeignKey("self", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=16)


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
    artist = models.CharField(max_length=16)
    etc = models.CharField(max_length=64)

    # Album
    author = models.CharField(max_length=16)
    isbn = models.CharField(max_length=32)

    # Movie
    director = models.CharField(max_length=16)
    actor = models.CharField(max_length=32)
