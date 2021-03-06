from django.conf import settings
from django.db import models
from yandex_geocoder import Client


class Address(models.Model):
    """A model represents users address."""

    user = models.ForeignKey(
        to='users.User',
        verbose_name='пользователь',
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    name = models.CharField(
        verbose_name='название',
        max_length=64
    )
    street = models.CharField(
        verbose_name='улица',
        max_length=80
    )
    city = models.CharField(
        verbose_name='город',
        max_length=50
    )
    state = models.CharField(
        verbose_name='Край/Область',
        max_length=33
    )
    longitude = models.DecimalField(
        max_digits=18,
        decimal_places=3,
    )
    latitude = models.DecimalField(
        max_digits=18,
        decimal_places=3,
    )
    is_default = models.BooleanField(
        verbose_name='Основной'
    )

    def __str__(self):
        return f'{self.name}'

    def set_coordinates(self):
        """Set coords to `longitude` and `latitude` fields
        before saving model instance.
        """
        client = Client(api_key=settings.YANDEX_GEOCODER_KEY)
        address = f'Россия, {self.state}, {self.city}, {self.street}'
        self.longitude, self.latitude = client.coordinates(address)

    def save(self, *args, **kwargs):
        self.set_coordinates()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'
        unique_together = (('is_default', 'user'),)
