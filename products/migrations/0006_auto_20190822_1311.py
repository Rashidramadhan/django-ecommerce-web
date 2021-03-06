# Generated by Django 2.2.4 on 2019-08-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190822_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery_option',
            old_name='order_id',
            new_name='orderID',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='delivery_adress',
            new_name='delivery_address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='userID',
        ),
        migrations.RenameField(
            model_name='order_history',
            old_name='order_id',
            new_name='orderID',
        ),
        migrations.RenameField(
            model_name='order_product',
            old_name='order_id',
            new_name='orderID',
        ),
        migrations.RenameField(
            model_name='order_product',
            old_name='product_id',
            new_name='product_code',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='order_id',
            new_name='orderID',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand_id',
            new_name='brandID',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_type_id',
            new_name='product_typeID',
        ),
        migrations.RenameField(
            model_name='stock_level',
            old_name='product_id',
            new_name='product_code',
        ),
        migrations.AddField(
            model_name='brand',
            name='brandID',
            field=models.CharField(default='new', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='orderID',
            field=models.CharField(default='order1', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='p001', max_length=20),
        ),
        migrations.AddField(
            model_name='product_type',
            name='product_typeID',
            field=models.CharField(default='pro', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='userID',
            field=models.CharField(default='user', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(),
        ),
    ]
