# Generated by Django 4.2.3 on 2024-03-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_data_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sector',
            field=models.CharField(max_length=256),
        ),
    ]
