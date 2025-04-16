from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Packet, TablytsySpivstavleny

def packet_list(request):
    """
    Представлення для виведення списку всіх пакетів.
    """
    packets = Packet.objects.all()
    return render(request,
                  'pmgapp/packet_list.html',
                  {'packets': packets})

def packet_detail(request, packet_number):
    try:
        packet = Packet.objects.get(packet_number=packet_number)
    except Packet.DoesNotExist:
        raise Http404("No Packet found.")
    
    return render(request,
                'pmgapp/packet_detail.html',
                {'packet': packet})

def packet_vymohy(request, packet_number):
    packet = get_object_or_404(Packet, packet_number=packet_number)
    return render(request,
                  'pmgapp/vymohy.html',
                  {'packet': packet})

def packet_tab(request, packet_number):
    packet = get_object_or_404(Packet, packet_number=packet_number)
    tablytsi = TablytsySpivstavleny.objects.filter(packet=packet)
    return render(request,
                  'pmgapp/tab.html',
                  {'tablytsi': tablytsi, 'packet': packet})
