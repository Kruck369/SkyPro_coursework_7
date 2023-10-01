import os

from celery import shared_task
from telegram import Bot


@shared_task
def send_notification(user_id, message):
    bot = Bot(token=os.getenv('TELEGRAM_BOT_KEY'))

    bot.send_message(chat_id=user_id, text=message)
