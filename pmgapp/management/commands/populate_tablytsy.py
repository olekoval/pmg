import pandas as pd
from django.core.management.base import BaseCommand
from pmgapp.models import Packet, TablytsySpivstavleny

df = pd.read_excel("pmgapp/static/packets/packet_9.xlsx")
df = df.fillna('-')

def transform_item(item):
    subitem = item.split('-')
    return f"{subitem[1].strip()} - {subitem[2].strip()}"

col = df['posluga'].tolist()
posluga_list = [transform_item(item) for item in col if transform_item(item)]
nk25_list = df['nk25'].tolist()
nk26_list = df['nk26'].tolist()
dodatoc_list = df['dodatoc'].tolist()

class Command(BaseCommand):
    help = 'Заповнює таблицю TablytsySpivstavleny даними зі списків'

    def handle(self, *args, **kwargs):
        try:
            packet_obj = Packet.objects.get(packet_number=9)
            for i in range(len(posluga_list)):
                TablytsySpivstavleny.objects.create(
                    packet=packet_obj,
                    posluga=posluga_list[i],
                    nk25=nk25_list[i],
                    nk26=nk26_list[i],
                    dodatoc=dodatoc_list[i]
                )
            self.stdout.write(self.style.SUCCESS('Дані успішно додано до таблиці TablytsySpivstavleny.'))
        except Packet.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Помилка: Пакет з packet_number=9 не знайдено.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Виникла помилка: {e}'))
