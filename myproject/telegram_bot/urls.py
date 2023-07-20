from django.urls import path

from myproject.telegram_bot import bot

app_name = 'telegram_bot'

urlpatterns = [
    path('bot/', bot.setup_telegram_bot),
]
