# Generated by Django 2.2.1 on 2019-05-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20190524_0154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='ovqatlar',
            new_name='birinchi_ovqatlar',
        ),
        migrations.AddField(
            model_name='client',
            name='ikkinchi_ovqatlar',
            field=models.CharField(blank=True, choices=[('osh', 'oshlar'), ('bishteks', 'bishteks'), ('asortiment', 'asortiment')], max_length=12, null=True),
        ),
    ]
