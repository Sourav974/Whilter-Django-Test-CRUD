# Generated by Django 4.0.4 on 2022-05-26 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_logoslot_textbox'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogoSlot',
        ),
        migrations.DeleteModel(
            name='TextBox',
        ),
    ]
