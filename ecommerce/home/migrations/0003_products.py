# Generated by Django 4.2.3 on 2023-07-31 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default='Some default description', max_length=500)),
                ('quntity', models.IntegerField()),
                ('orginal_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('selling_price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=defualt,1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=defualt,1=Hidden')),
                ('category', models.ForeignKey(default='Uncategorized', on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
