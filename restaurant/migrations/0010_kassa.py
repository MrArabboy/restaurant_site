# Generated by Django 2.2.1 on 2019-05-26 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_auto_20190525_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='kassa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hisob', models.ManyToManyField(to='restaurant.client')),
            ],
        ),
    ]
