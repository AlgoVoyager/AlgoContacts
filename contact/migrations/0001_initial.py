# Generated by Django 3.2.7 on 2022-02-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=12)),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]