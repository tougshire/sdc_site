# Generated by Django 5.0.3 on 2024-04-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0026_articlecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='rack',
            name='collapse',
            field=models.BooleanField(default=True, help_text='Collapse if there are no hangers/articles', verbose_name='collapse'),
        ),
        migrations.AddField(
            model_name='section',
            name='collapse',
            field=models.BooleanField(default=True, help_text='Collapse if there are no racks', verbose_name='collapse'),
        ),
    ]
