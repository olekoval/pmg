"""Видаляє всі дані з таблиці TablytsySpivstavleny"""

from django.core.management.base import BaseCommand
from pmgapp.models import TablytsySpivstavleny

class Command(BaseCommand):
    help = 'Видаляє всі дані з таблиці TablytsySpivstavleny'

    def handle(self, *args, **kwargs):
        try:
            deleted_count, _ = TablytsySpivstavleny.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Успішно видалено {deleted_count} записів з таблиці TablytsySpivstavleny.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Виникла помилка при видаленні даних: {e}'))
