from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

# Cada grupo recebe só as permissões do app person listadas aqui.
GROUPS = {
    'Vendedor': ['view_employee', 'add_employee'],
    'Gerente': [
        'view_employee',
        'add_employee',
        'change_employee',
        'delete_employee',
        'view_salary',
    ],
}


class Command(BaseCommand):
    help = 'Cria os grupos Vendedor e Gerente com as permissões de cada um.'

    def handle(self, *args, **options):
        for name, codenames in GROUPS.items():
            group, _ = Group.objects.get_or_create(name=name)
            permissions = Permission.objects.filter(
                content_type__app_label='person',
                codename__in=codenames,
            )
            group.permissions.set(permissions)
            self.stdout.write(self.style.SUCCESS(f'{name}: {permissions.count()} permissões'))
