from django.db import models
import uuid


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=60, verbose_name='nombre')

    class Meta:
        verbose_name = 'Paìs'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name
