# Generated by Django 3.0.6 on 2020-07-01 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20200630_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='allowances',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='basic_salary',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='hra',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='emp_id',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.FloatField()),
                ('hra', models.FloatField(blank=True, null=True)),
                ('pf', models.FloatField(blank=True, null=True)),
                ('da', models.FloatField(blank=True, null=True)),
                ('other_allowances', models.FloatField(blank=True, null=True)),
                ('net_salary', models.FloatField()),
                ('teacher_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
    ]
