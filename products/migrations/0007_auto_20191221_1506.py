# Generated by Django 3.0 on 2019-12-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20191221_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('S', 'Shirt'), ('TS', 'T-Shirt'), ('H', 'Hoodie'), ('PJ', 'Panjabi')], max_length=100),
        ),
    ]
