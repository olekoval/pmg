
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('packets_pmg/', include('pmgapp.urls', namespace='packet')),
    path('', include('pmgapp.urls', namespace='packet')),
]






