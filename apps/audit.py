from django.conf import settings
import uuid
from django.db import models
from rest_framework import viewsets


class Audit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Creado por', null=True, blank=True,
                                   editable=False, related_name='%(app_label)s_%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Actualizado por', editable=False,
                                   null=True, blank=True, related_name='%(app_label)s_%(class)s_updated_by')

    class Meta:
        abstract = True


class AuditView(viewsets.ModelViewSet):

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(updated_by=self.request.user)
