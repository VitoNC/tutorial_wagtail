# Generated by Django 3.2.11 on 2022-03-02 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_pelipage_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelipage',
            name='ids',
        ),
    ]
