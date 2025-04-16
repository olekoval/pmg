from django.contrib import admin
from .models import Packet, TablytsySpivstavleny

@admin.register(Packet)
class PacketAdmin(admin.ModelAdmin):
    list_display = ['title', 'packet_number', 'postanova', 'updated']
    list_filter = ['packet_number']
    search_fields = ['packet_number']


@admin.register(TablytsySpivstavleny)
class TablytsySpivstavlenyAdmin(admin.ModelAdmin):
    list_display = ['posluga', 'packet', 'nk25', 'nk26', 'dodatoc'] # Показувати ці поля у списку
    list_filter = ['packet'] # Додати фільтр за пакетом
    search_fields = ['posluga', 'nk25', 'nk26'] # Додати пошук за цими полями
    
    # дозволити незаповнювати необов'язкові поля
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['nk25'].required = False
        form.base_fields['nk26'].required = False
        form.base_fields['dodatoc'].required = False
        return form