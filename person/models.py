from django.db import models

from core.models import ActiveModel, TimeStampedModel


class Employee(TimeStampedModel, ActiveModel):
    """Funcionário da empresa. O salário só aparece para quem tem a permissão view_salary."""

    class Role(models.TextChoices):
        SELLER = 'seller', 'Vendedor'
        MANAGER = 'manager', 'Gerente'

    name = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail', unique=True)
    role = models.CharField('cargo', max_length=20, choices=Role)
    salary = models.DecimalField('salário', max_digits=10, decimal_places=2)
    hired_on = models.DateField('admissão')

    class Meta:
        ordering = ('name',)
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'
        permissions = [
            ('view_salary', 'Pode ver o salário'),
        ]

    def __str__(self):
        return self.name
