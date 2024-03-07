# Generated by Django 4.2.4 on 2024-03-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdc_site', '0013_auto_20240303_1906'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tagory',
            new_name='Tag',
        ),
        migrations.RemoveField(
            model_name='articletagory',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articletagory',
            name='tagory',
        ),
        migrations.AlterModelOptions(
            name='segment',
            options={'ordering': ('column', 'order', 'title')},
        ),
        migrations.AddField(
            model_name='segment',
            name='content_classes',
            field=models.CharField(blank=True, default='segment-content uldoc', help_text='HTML classes to be applied to the content (default: segment-content uldoc)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='content_format',
            field=models.CharField(choices=[('markdown', 'Markdown'), ('html', 'HTML'), ('plaintext', 'Plain Text')], default='markdown', help_text='The format used for rendering the content', max_length=12),
        ),
        migrations.AddField(
            model_name='segment',
            name='slug',
            field=models.SlugField(default='', help_text='The slug for use in URLs', max_length=100, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='segment',
            name='title',
            field=models.CharField(help_text='The name of the segment.', max_length=100, verbose_name='title'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleTagory',
        ),
    ]
