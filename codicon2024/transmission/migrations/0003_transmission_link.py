# Generated by Django 5.0.3 on 2024-03-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transmission', '0002_transmission_categoria_transmission_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmission',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
