# Generated by Django 4.0.1 on 2022-05-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_artiles_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='anons',
            field=models.CharField(max_length=1500, verbose_name='Анонс'),
        ),
    ]
