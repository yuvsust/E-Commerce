# Generated by Django 3.0 on 2019-12-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20191221_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(max_length=100),
        ),
    ]
