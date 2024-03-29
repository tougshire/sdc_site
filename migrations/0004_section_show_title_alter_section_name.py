# Generated by Django 4.2.4 on 2024-03-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0003_alter_case_show_article_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='show_title',
            field=models.BooleanField(default=True, help_text='Show the title of the section ', verbose_name='show title'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(help_text='The title of the section.', max_length=100, verbose_name='name'),
        ),
    ]
