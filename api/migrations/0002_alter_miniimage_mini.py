# Generated by Django 4.1.1 on 2022-09-12 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniimage',
            name='mini',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mini_images', to='api.mini'),
        ),
    ]