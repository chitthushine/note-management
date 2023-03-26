from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Initialize admin user'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('initialize admin user ...'))

        # superuser, for accessing django admin page.
        sys_admin, sys_admin_created = User.objects.get_or_create(username='admin')
        if sys_admin_created:
            self.stdout.write(self.style.NOTICE('setup superuser ...'))
            sys_admin.set_password('bh>R4!S]')
            sys_admin.is_superuser = True
            sys_admin.is_staff = True
            sys_admin.save()
            self.stdout.write(self.style.NOTICE('setup superuser finished !!!'))