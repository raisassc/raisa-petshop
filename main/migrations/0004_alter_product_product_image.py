# Generated by Django 5.1.1 on 2024-09-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_catfood_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]
