# Generated by Django 4.0.1 on 2022-05-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_telegram'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=1500, verbose_name='Описание')),
                ('full_text', models.TextField(verbose_name='Подробности')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': '1C',
                'verbose_name_plural': '1C',
            },
        ),
    ]
