# Generated by Django 2.2.1 on 2019-05-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]