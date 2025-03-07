# Generated by Django 4.1.2 on 2024-06-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0037_alter_mainattribute_create_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mainattribute",
            name="create_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="创建时间"
            ),
        ),
        migrations.AlterField(
            model_name="mainattribute",
            name="modify_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="修改时间"
            ),
        ),
        migrations.AlterField(
            model_name="storeassign",
            name="create_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="创建时间"
            ),
        ),
        migrations.AlterField(
            model_name="storeassign",
            name="modify_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="修改时间"
            ),
        ),
        migrations.AlterField(
            model_name="storecomparable",
            name="create_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="创建时间"
            ),
        ),
        migrations.AlterField(
            model_name="storecomparable",
            name="modify_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="修改时间"
            ),
        ),
        migrations.AlterField(
            model_name="storemapping",
            name="create_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="创建时间"
            ),
        ),
        migrations.AlterField(
            model_name="storemapping",
            name="modify_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="修改时间"
            ),
        ),
    ]
