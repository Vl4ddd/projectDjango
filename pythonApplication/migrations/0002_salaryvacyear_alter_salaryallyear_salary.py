# Generated by Django 5.0.1 on 2024-01-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonApplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryVacYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.TextField()),
                ('salary', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
            options={
                'db_table': 'salary_by_year_vac',
            },
        ),
        migrations.AlterField(
            model_name='salaryallyear',
            name='salary',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]