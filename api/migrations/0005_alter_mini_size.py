# Generated by Django 4.1.1 on 2022-09-14 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_mini_creator_model_id_mini_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mini',
            name='size',
            field=models.CharField(choices=[('T', 'Tiny'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('H', 'Huge'), ('G', 'Gargantuan'), ('C', 'Colossal')], default='M', max_length=1),
        ),
    ]