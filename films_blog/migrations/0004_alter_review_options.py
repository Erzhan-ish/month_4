# Generated by Django 5.1.3 on 2024-12-12 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films_blog', '0003_alter_review_stars'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
