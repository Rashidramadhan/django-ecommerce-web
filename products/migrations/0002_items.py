# Generated by Django 2.2.4 on 2019-08-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_category', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=20)),
                ('item_price', models.CharField(max_length=10)),
                ('item_description', models.CharField(max_length=300)),
                ('means_of_payment', models.CharField(max_length=50)),
            ],
        ),
    ]
