import uuid

from django.conf import settings
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from src.addition.abstract_model import CreatedAt, UpdatedAt
from src.core.enums.LanguageEnum import Language


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_of_birth = models.PositiveSmallIntegerField(null=True, blank=True)
    year_of_death = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"],
                name="unique_author_name",
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(CreatedAt, UpdatedAt):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    language = models.CharField(choices=Language.choices(), default=Language.EU, max_length=9)
    pages = models.IntegerField(validators=[
        MaxValueValidator(2000),
        MinValueValidator(1)
    ])
    published_at = models.IntegerField(validators=[
        RegexValidator(
            regex="^[0-9]{4}$",
            message="Enter a valid registration year in the format '2024'.",
            code="invalid_registration"
            ),
    ])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userName')
    cover = models.ImageField(
        verbose_name="Cover image",
        upload_to="media/books/covers/",
        blank=True,
        help_text="The cover image of book",
    )

    def __str__(self):
        return self.name
