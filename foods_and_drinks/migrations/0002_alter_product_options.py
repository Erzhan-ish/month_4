# Generated by Django 5.1.3 on 2024-12-12 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods_and_drinks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]