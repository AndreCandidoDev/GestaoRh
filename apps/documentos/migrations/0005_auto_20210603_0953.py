# Generated by Django 2.2 on 2021-06-03 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_documento_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='documentos'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='descricao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
        ),
    ]
