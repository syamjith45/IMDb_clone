# Generated by Django 4.2.9 on 2024-01-11 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0.0)),
                ('review', models.CharField(blank=True, max_length=250, null=True)),
                ('rated_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
