# Generated by Django 4.2.4 on 2024-03-07 14:36
import django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "sdc_site",
            "0020_remove_column_content_column_content_above_articles_and_more",
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Column",
            new_name="Case",
        ),
        migrations.RenameModel(
            old_name="SectionColumn",
            new_name="SectionCase",
        ),
        migrations.AlterModelOptions(
            name="article",
            options={"ordering": ("case", "order", "title")},
        ),
        migrations.RenameField(
            model_name="article",
            old_name="column",
            new_name="case",
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(
                blank=True,
                help_text="The content of the case.  Expected to usually include an iframe or series of iframes",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="order",
            field=models.IntegerField(
                default=0,
                help_text="The order that the article would appear in the case",
                verbose_name="order",
            ),
        ),
        migrations.AlterField(
            model_name="case",
            name="content_above_articles",
            field=models.CharField(
                blank=True,
                help_text="The content of the case above any included articles",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="case",
            name="content_below_articles",
            field=models.CharField(
                blank=True,
                help_text="The content of the case below any included articles",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="case",
            name="name",
            field=models.CharField(
                help_text="The name of the case.", max_length=100, verbose_name="name"
            ),
        ),
        migrations.AlterField(
            model_name="case",
            name="width",
            field=models.IntegerField(
                default=1,
                help_text="The width of the case in multiples of how big it is compared to the narrowest case",
                verbose_name="width",
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="content_after",
            field=models.TextField(
                blank=True, help_text="content to be displayed below the cases"
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="content_before",
            field=models.TextField(
                blank=True, help_text="content to be displayed above the cases"
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="page",
            field=models.ForeignKey(
                blank=True,
                help_text="The page to which this case belongs",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sdc_site.page",
            ),
        ),
        migrations.RenameField(
            model_name="sectioncase",
            old_name="column",
            new_name="case",
        ),
        migrations.AlterField(
            model_name="sectioncase",
            name="case",
            field=models.ForeignKey(
                help_text="The case which appears in the section",
                on_delete=django.db.models.deletion.CASCADE,
                to="sdc_site.case",
            ),
        ),
        migrations.AlterField(
            model_name="sectioncase",
            name="section",
            field=models.ForeignKey(
                help_text="The section to which the case belongs",
                on_delete=django.db.models.deletion.CASCADE,
                to="sdc_site.section",
            ),
        ),
    ]