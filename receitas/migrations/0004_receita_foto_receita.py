# Generated by Django 4.1.3 on 2022-11-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receitas", "0003_receita_publicada"),
    ]

    operations = [
        migrations.AddField(
            model_name="receita",
            name="foto_receita",
            field=models.ImageField(blank=True, upload_to="fotos/%d/%m/%Y/"),
        ),
    ]
