from django.contrib.auth.models import AbstractUser
from django.db import models


class Address(models.Model):
    city = models.CharField(verbose_name="도시", max_length=64)
    street = models.CharField(verbose_name="도로명 주소", max_length=64)
    zipcode = models.CharField(verbose_name="우편번호", max_length=32)

    class Meta:
        abstract = True


class Member(AbstractUser, Address):
    def __str__(self):
        return self.username
