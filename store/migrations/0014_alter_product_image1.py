# Generated by Django 5.0.3 on 2024-04-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_product_video1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]