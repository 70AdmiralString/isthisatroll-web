# Generated by Django 3.1.7 on 2021-03-26 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Redditor',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('analysis_date', models.DateTimeField(verbose_name='date analyzed')),
                ('result', models.FloatField()),
            ],
        ),
    ]
