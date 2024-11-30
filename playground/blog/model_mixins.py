from django.contrib.auth.models import User

from typing import Protocol


class BloggerProtocol(Protocol):
    user: User


class BloggerMixin:
    @property
    def fullname(self: BloggerProtocol) -> str:
        return f'{self.user.last_name} {self.user.first_name}'
