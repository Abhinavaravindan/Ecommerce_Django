# Generated by Django 4.2.3 on 2023-07-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default='default_product_image.jpg', upload_to='product_images'),
        ),
    ]
