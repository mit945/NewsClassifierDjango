# Generated by Django 3.0.8 on 2020-08-20 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_category_prob_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='viz',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]