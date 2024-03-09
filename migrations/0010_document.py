# Generated by Django 4.2.4 on 2024-03-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0009_article_iframe_height'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the document for reference within this application', max_length=50, verbose_name='name')),
                ('doc_file', models.FileField(help_text='The file to be uploaded', upload_to='documents')),
            ],
        ),
    ]
