# Generated by Django 3.0.1 on 2020-02-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20200121_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='dt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]