# Generated by Django 2.1.3 on 2018-12-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtenapp', '0003_auto_20181210_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='creator',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
