from django.apps import AppConfig
from django.db import migrations, models

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'



class Migration(migrations.Migration):

    dependencies = [
        # Previous migrations' dependencies if any
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='product_images'),
        ),
    ]
