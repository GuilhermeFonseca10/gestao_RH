# Generated by Django 4.1.2 on 2022-11-03 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Funcionarios", "0002_funcionario_departamentos_funcionario_empresa_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
