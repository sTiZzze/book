from __future__ import absolute_import, unicode_literals

from celery import shared_task

from src.book.services import send_email


@shared_task
def send_email_task():
    send_email.delay()
