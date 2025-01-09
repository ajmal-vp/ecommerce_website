# Generated by Django 5.1.4 on 2025-01-07 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_2_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='email',
        ),
        migrations.AddField(
            model_name='seller',
            name='product_category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]
