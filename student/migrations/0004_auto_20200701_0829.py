# Generated by Django 3.0.6 on 2020-07-01 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_customuser_is_user_deleted'),
        ('student', '0003_delete_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.ClassName'),
        ),
    ]
