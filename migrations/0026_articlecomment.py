# Generated by Django 5.0.3 on 2024-04-09 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0025_article_read_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articlecomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your name', max_length=80)),
                ('email', models.EmailField(help_text='Your email', max_length=254)),
                ('content', models.TextField()),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sdc_site.article')),
            ],
            options={
                'ordering': ['when'],
            },
        ),
    ]
