# Generated by Django 2.2.4 on 2019-09-02 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikesharing', '0011_auto_20190911_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'get_latest_by': 'reported_at'},
        ),
        migrations.RemoveField(
            model_name='bike',
            name='current_position',
        ),
    ]