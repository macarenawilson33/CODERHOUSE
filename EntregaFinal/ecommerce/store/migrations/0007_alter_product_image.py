# Generated by Django 4.2.13 on 2024-06-19 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_orderstatus_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default/default_product.jpg', upload_to='upload/product/'),
        ),
    ]