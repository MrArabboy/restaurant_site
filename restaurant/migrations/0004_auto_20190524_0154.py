# Generated by Django 2.2.1 on 2019-05-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20190524_0136'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ofitsiant',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='birinchi_ovqat',
            new_name='ovqatlar',
        ),
        migrations.AlterField(
            model_name='client',
            name='ichimlik',
            field=models.CharField(blank=True, choices=[('Pepsi', 'Pepsi'), ('Coca Cola', 'Coca Cola'), ('kofe', 'kofe')], max_length=12, null=True),
        ),
    ]
