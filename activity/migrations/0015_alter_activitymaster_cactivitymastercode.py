# Generated by Django 5.0.6 on 2024-11-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0014_alter_activitymaster_cactivitymastercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitymaster',
            name='cActivityMasterCode',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]