import pandas as pd
from django.core.management.base import BaseCommand
from pmgapp.models import Packet, TablytsySpivstavleny

df = pd.read_excel("../../static/packets/packet_9.xlsx")
df = df.iloc[4:, :]

def transform_item(item):
    subitem = item.split('-') 
    return f"{subitem[1].strip()} - {subitem[2].strip()}"


col = df['posluga'].tolist()
posluga = [transform_item(item) for item in col if transform_item(item)]
nk25 = df['nk25'].tolist()
nk26 = df['nk26'].tolist()
dodatoc = df['dodatoc'].tolist()

class Command(BaseCommand):
    help = 'Заповнює таблицю TablytsySpivstavleny даними зі списків'

    def handle(self, *args, **kwargs):
        posluga = posluga
        nk25 = nk25
        nk26 = nk26
        dodatoc = dodatoc

        try:
            packet_obj = Packet.objects.get(packet_number=9)
            for i in range(len(posluga)):
                TablytsySpivstavleny.objects.create(
                    packet=packet_obj,
                    posluga=posluga[i],
                    nk25=nk25[i],
                    nk26=nk26[i],
                    dodatoc=dodatoc[i]
                )
            self.stdout.write(self.style.SUCCESS('Дані успішно додано до таблиці TablytsySpivstavleny.'))
        except Packet.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Помилка: Пакет з packet_number=9 не знайдено.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Виникла помилка: {e}'))
