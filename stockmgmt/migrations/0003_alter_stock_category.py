# Generated by Django 4.0.5 on 2022-06-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0002_alter_stock_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
