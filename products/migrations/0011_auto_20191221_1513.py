# Generated by Django 3.0 on 2019-12-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20191221_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('S', 'Shirt'), ('TS', 'T Shirt'), ('H', 'Hoodie'), ('PJ', 'Panjabi')], max_length=255),
        ),
    ]
