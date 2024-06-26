# Generated by Django 4.2.4 on 2023-10-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_migrate_age_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('category', models.CharField(default='empty', max_length=20)),
            ],
        ),
    ]
