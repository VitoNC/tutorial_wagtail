# Generated by Django 3.2.11 on 2022-02-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_libro_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='synopsis',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
