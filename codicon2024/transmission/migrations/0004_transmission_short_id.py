# Generated by Django 5.0.3 on 2024-03-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transmission', '0003_transmission_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmission',
            name='short_id',
            field=models.CharField(blank=True, editable=False, max_length=10, unique=True),
        ),
    ]
