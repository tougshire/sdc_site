# Generated by Django 5.0.3 on 2024-04-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0023_rename_rackarticle_hanger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(help_text='The name or slug for use in URLs and within the application.  Note: Auto-generated value may not be unique. Uniquness and format are checked after submit', max_length=100, unique=True, verbose_name='name/slug'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='The title of the article.', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='document',
            name='slug',
            field=models.SlugField(help_text='The name or slug for use in URLs and within the application.  Note: Auto-generated value may not be unique. Uniquness and format are checked after submit', max_length=100, unique=True, verbose_name='name/slug'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, help_text='The title to be displayed with document.  It may or may not correspond to anything in the document itself. (can be blank)', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(help_text='The name or slug for use in URLs and within the application.  Note: Auto-generated value may not be unique. Uniquness and format are checked after submit', max_length=100, unique=True, verbose_name='name/slug'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, help_text='The title of the page. to be displayed (can be blank)', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='rack',
            name='slug',
            field=models.SlugField(help_text='The name or slug for use in URLs and within the application.  Note: Auto-generated value may not be unique. Uniquness and format are checked after submit', max_length=100, unique=True, verbose_name='name/slug'),
        ),
        migrations.AlterField(
            model_name='rack',
            name='title',
            field=models.CharField(blank=True, help_text='The title of the rack to be displayed (can be blank)', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='section',
            name='display',
            field=models.CharField(choices=[('Y', 'Normal'), ('P', 'Preview Only'), ('N', 'Do not display')], default='Y', help_text='How the section should be displayed', max_length=2, verbose_name='display when'),
        ),
        migrations.AlterField(
            model_name='section',
            name='show_title',
            field=models.BooleanField(default=True, help_text='If the title of this section should be shown (if not blank)', verbose_name='show title'),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(help_text='The name or slug for use in URLs and within the application.  Note: Auto-generated value may not be unique. Uniquness and format are checked after submit', max_length=100, unique=True, verbose_name='name/slug'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(blank=True, help_text='The title of the page. to be displayed (can be blank)', max_length=200, verbose_name='title'),
        ),
    ]