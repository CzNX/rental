# Generated by Django 3.0.1 on 2020-02-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20200216_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='type',
            field=models.CharField(blank=True, choices=[('C', 'Cheap'), ('A', 'Average'), ('E', 'Expensive')], max_length=1, null=True),
        ),
    ]
