from django.db import models


class CreatedAt(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAt(models.Model):
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

