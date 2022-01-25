from django.db import models

# Create your models here.
from django.urls import reverse


class Fighter(models.Model):

    first_name = models.CharField(max_length=100, help_text='First name of the fighter')
    last_name = models.CharField(max_length=100, help_text='Last name of the fighter')
    nickname = models.CharField(max_length=100, help_text='Nickname of the fighter, if exist', null=True, blank=True)
    birthday = models.DateField('Birthday', null=True, blank=True)
    start_carrier = models.DateField('Start carrier', null=True, blank=True)
    end_carrier = models.DateField('End carrier', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_absolute_url(self):
        return reverse('fighter-detail', args=[str(self.id)])

