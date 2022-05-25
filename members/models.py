from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from .exceptions import MemberException


class Address(models.Model):
    city = models.CharField(verbose_name="도시", max_length=64)
    street = models.CharField(verbose_name="도로명 주소", max_length=64)
    zipcode = models.CharField(verbose_name="우편번호", max_length=32)

    class Meta:
        abstract = True


class MemberManager(UserManager):
    def join(self, password, username, **kwargs) -> int:
        """
        회원 가입
        """
        self.validate_duplicate_member(username=username)
        member = self.create_user(username=username, **kwargs)
        member.set_password(password)
        member.save()
        return member.pk

    def validate_duplicate_member(self, username: str) -> None:
        """
        중복 회원 검증
        """
        if self.filter(username=username).exists():
            raise MemberException("이미 존재하는 회원입니다.")


class Member(AbstractUser, Address):
    def __str__(self):
        return self.username

    objects = MemberManager()

    @property
    def address(self):
        return {"city": self.city, "street": self.street, "zipcode": self.zipcode}