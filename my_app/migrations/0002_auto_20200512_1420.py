# Generated by Django 2.1.7 on 2020-05-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'searches'},
        ),
        migrations.AlterField(
            model_name='search',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(max_length=20),
        ),
    ]
