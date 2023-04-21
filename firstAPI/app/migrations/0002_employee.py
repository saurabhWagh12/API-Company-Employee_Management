# Generated by Django 4.1.5 on 2023-04-21 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('about', models.TextField(blank=True)),
                ('position', models.CharField(choices=[('SDE1', 'SDE1'), ('SDE2', 'SDE2'), ('SDE3', 'SDE3'), ('Manager', 'Manager'), ('Product Manager', 'Product Manager')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
    ]