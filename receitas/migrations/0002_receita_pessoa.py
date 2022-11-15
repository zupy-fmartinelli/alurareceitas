# Generated by Django 4.1.3 on 2022-11-07 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("receitas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="receita",
            name="pessoa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
            preserve_default=False,
        ),
    ]
