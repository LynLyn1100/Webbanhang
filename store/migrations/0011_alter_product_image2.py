# Generated by Django 5.0.3 on 2024-04-10 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_product_image3_alter_product_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]