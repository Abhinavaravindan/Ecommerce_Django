# Generated by Django 4.2.3 on 2023-09-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
