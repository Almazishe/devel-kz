import uuid
from django.db import models


class BaseModel(models.Model):
    """
        BaseModel interface:
            - Adds uuid primary key field to models
    """
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='UUID',
    )

    class Meta:
        abstract = True
        ordering = ('-uuid',)

    def __str__(self) -> str:
        return str(self.uuid)


class DateModel(models.Model):
    """
        DateModel interface:
            - Adds created_at and updated_at fields to model
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        null=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения',
        null=True,
    )

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return str(self.created_at)


class Deletable(models.Model):
    """
        Deletable interface model:
            - Adds is_deleted boolean field to models
    """
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="Удален"
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.is_deleted}'
