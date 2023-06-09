# Generated by Django 4.1.4 on 2023-04-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('NON IT', 'NON IT'), ('Consultancy', 'Consultancy')], max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
