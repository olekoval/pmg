from django.contrib import admin
from .models import Packet

@admin.register(Packet)
class PacketAdmin(admin.ModelAdmin):
    list_display = ['title', 'packet_number', 'postanova', 'updated']
    list_filter = ['packet_number']
    search_fields = ['packet_number']
