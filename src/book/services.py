from __future__ import absolute_import, unicode_literals

from datetime import timedelta

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

from src.book.models import Book


@shared_task
def send_email():
    users = User.objects.exclude(email__exact='')
    now = timezone.now()
    ten_minutes_ago = now - timedelta(minutes=60)
    recent_books = Book.objects.filter(created_date__gte=ten_minutes_ago).values_list('name', flat=True)
    if recent_books:
        for user in users:
            msg = EmailMultiAlternatives(
                subject='Recent Books',
                body=f'Hi, {user} . It is a new books for you:\n' + '\n'.join(list(recent_books)),
                from_email='test@example.com',
                to=[user.email,],
            )
            msg.send()
