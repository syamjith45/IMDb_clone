# Generated by Django 4.2.9 on 2024-01-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(default='')),
                ('cover', models.ImageField(upload_to='movies/')),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
    ]