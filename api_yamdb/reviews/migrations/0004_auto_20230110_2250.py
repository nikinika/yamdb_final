# Generated by Django 3.2 on 2023-01-10 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230110_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('category',)},
        ),
    ]
