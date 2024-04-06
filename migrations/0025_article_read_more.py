# Generated by Django 5.0.3 on 2024-04-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0024_alter_article_slug_alter_article_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read_more',
            field=models.CharField(blank=True, default='Read More', help_text='Text to display in a read more link', max_length=50),
        ),
    ]
