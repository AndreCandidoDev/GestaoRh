# Generated by Django 2.2 on 2021-05-31 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20210531_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
