# Generated by Django 4.2.4 on 2024-03-05 15:23

from django.db import migrations


def populate_slug(apps, schema_editor):
    Segment = apps.get_model("sdc_site", "Segment")

    for segment in Segment.objects.all():
        segment.slug = segment.title.replace(" ", "").lower() + "_" + str(segment.pk)
        segment.save()


class Migration(migrations.Migration):

    dependencies = [
        ("sdc_site", "0014_rename_tagory_tag_remove_articletagory_article_and_more"),
    ]

    operations = [migrations.RunPython(populate_slug)]
