# Generated by Django 5.0.3 on 2024-05-15 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0030_remove_article_width_article_content_classes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_image',
            field=models.ForeignKey(blank=True, help_text='The image to be displayed when linking to the article on social media', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sdc_site.sdcimage'),
        ),
    ]
