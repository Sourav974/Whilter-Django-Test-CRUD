# Generated by Django 4.0.4 on 2022-05-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_url', models.FileField(null=True, upload_to='media')),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_id', models.IntegerField()),
                ('component_url', models.FileField(null=True, upload_to='media')),
                ('component_start_time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Logos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_url', models.FileField(null=True, upload_to='media')),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('transition_in', models.CharField(max_length=20)),
                ('transition_out', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TextElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('font', models.CharField(max_length=30)),
                ('font_size', models.CharField(max_length=10)),
                ('position_x', models.CharField(max_length=10)),
                ('position_y', models.CharField(max_length=10)),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
            ],
        ),
    ]
