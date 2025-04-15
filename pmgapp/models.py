from django.db import models

class Packet(models.Model):
    title = models.CharField(max_length=150)
    packet_number = models.IntegerField(
        unique=True,
        primary_key=True
    )
    postanova = models.TextField(null=True) # запис може бути збережений без
                                            #обов'язкового заповнення цього поля
    vymohy = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    year = models.IntegerField(null=True)

    class Meta:
        ordering = ['packet_number']

    def __str__(self):
        return self.title
    
