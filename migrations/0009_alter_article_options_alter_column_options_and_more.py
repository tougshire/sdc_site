# Generated by Django 4.2.4 on 2024-03-02 12:39

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0008_alter_article_options_rename_name_article_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-date_for_dateline', '-when_updated')},
        ),
        migrations.AlterModelOptions(
            name='column',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='sectioncolumn',
            options={'ordering': ('section', 'order')},
        ),
        migrations.AlterModelOptions(
            name='tagory',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='column',
            name='order',
        ),
        migrations.RemoveField(
            model_name='tagory',
            name='order',
        ),
        migrations.AddField(
            model_name='article',
            name='date_for_dateline',
            field=models.DateField(default=datetime.date.today, help_text='The displayed date of the article', verbose_name='date'),
        ),
        migrations.AddField(
            model_name='article',
            name='when_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='The date the article was created', verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='when_updated',
            field=models.DateTimeField(auto_now=True, help_text='The date the article was updated', verbose_name='updated'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='order',
            field=models.IntegerField(default=1, help_text='The order that the item would appear in a menu', verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectioncolumn',
            name='order',
            field=models.IntegerField(default=0, help_text='The order that the section would appear on the page', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='article',
            name='order',
            field=models.IntegerField(default=0, help_text='The order that the column should appear on the page', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=0, help_text='The order that the page would appear in a list', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=0, help_text='The order that the section should appear on the page', verbose_name='order'),
        ),
    ]
