# Generated by Django 5.0.3 on 2024-05-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0029_sdcimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='width',
        ),
        migrations.AddField(
            model_name='article',
            name='content_classes',
            field=models.CharField(blank=True, help_text='Extra classes to be applied to the content when displayed', max_length=50, verbose_name='content classes'),
        ),
        migrations.AddField(
            model_name='hanger',
            name='expiration_date',
            field=models.DateField(blank=True, help_text='The date after which the article should no longer be displayed in the rack', null=True, verbose_name='expiration date'),
        ),
    ]
