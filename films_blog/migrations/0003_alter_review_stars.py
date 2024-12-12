# Generated by Django 5.1.3 on 2024-12-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_blog', '0002_alter_filmmodel_options_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], default='⭐', max_length=100, verbose_name='Поставьте оценку'),
        ),
    ]