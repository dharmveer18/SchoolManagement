# Generated by Django 3.0.6 on 2020-07-15 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_attendance_leaves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='reason',
            field=models.CharField(choices=[('N', 'None'), ('S', 'Sick Leave')], max_length=1),
        ),
    ]
