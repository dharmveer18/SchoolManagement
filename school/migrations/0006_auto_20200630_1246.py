# Generated by Django 3.0.6 on 2020-06-30 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20200630_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=30)),
                ('pin_code', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]