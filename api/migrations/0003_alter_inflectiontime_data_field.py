# Generated by Django 4.0.4 on 2022-05-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_component'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inflectiontime',
            name='data_field',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12),
            preserve_default=False,
        ),
    ]
