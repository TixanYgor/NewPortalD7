"""
Этот файл нужен для создания задач (D7).
Задачи это функции, которые можно использовать специальным обращением
и добавляя определенные параметры.
"""
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from celery.schedules import crontab
import time


@shared_task
def hello():
    time.sleep(10)
    print('Hello, world!')


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)


@shared_task
def email_task(subscriber_username, subscriber_email, html_content):
    msg = EmailMultiAlternatives(
                    subject=f'Здравствуй, {subscriber_username}. Новая статья в вашем разделе!',
                    from_email='TixanYgor@yandex.ru',
                    to=[subscriber_email]
                )
    msg.attach_alternative(html_content, 'text/html')


@shared_task
def weekly_email_task(subscriber_username, subscriber_email, html_content):
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {subscriber_username}, новые статьи за прошлую неделю в вашем разделе!',
        from_email='TixanYgor@yandex.ru',
        to=[subscriber_email]
    )

    msg.attach_alternative(html_content, 'text/html')
