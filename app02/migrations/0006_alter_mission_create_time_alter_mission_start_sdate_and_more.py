# Generated by Django 4.1.2 on 2024-06-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app02", "0005_alter_mission_create_time_alter_mission_start_sdate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mission",
            name="create_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="创建时间"
            ),
        ),
        migrations.AlterField(
            model_name="mission",
            name="start_sdate",
            field=models.DateField(
                default="2024-06-24 16:15:14", verbose_name="预测开始时间"
            ),
        ),
        migrations.AlterField(
            model_name="predresult",
            name="create_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="创建时间"
            ),
        ),
        migrations.AlterField(
            model_name="predresult",
            name="modify_time",
            field=models.DateTimeField(
                default="2024-06-24 16:15:14", verbose_name="修改时间"
            ),
        ),
    ]
