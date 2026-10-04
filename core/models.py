from django.db import models


class TimeStampedModel(models.Model):
    """Guarda quando o registro foi criado e quando foi alterado pela última vez."""

    created = models.DateTimeField('criado em', auto_now_add=True)
    modified = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    """Permite desativar um registro sem apagá-lo do banco."""

    active = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True
