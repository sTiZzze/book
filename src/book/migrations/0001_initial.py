# Generated by Django 5.0.7 on 2024-07-30 12:01

import uuid

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import src.core.enums.LanguageEnum


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('year_of_birth', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('year_of_death', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('language', models.CharField(choices=[('Русский', 'RU'), ('English', 'EU'), ('Poland', 'PL'), ('Germany', 'DE')], default=src.core.enums.LanguageEnum.Language['EU'], max_length=9)),
                ('pages', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(1)])),
                ('published_at', models.IntegerField(validators=[django.core.validators.RegexValidator(code='invalid_registration', message="Enter a valid registration year in the format '2024'.", regex='^[0-9]{4}$')])),
                ('cover', models.ImageField(blank=True, help_text='The cover image of book', upload_to='books/covers/', verbose_name='Cover image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='unique_author_name'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='book.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userName', to=settings.AUTH_USER_MODEL),
        ),
    ]
