# Generated by Django 3.0.4 on 2020-04-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200403_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]