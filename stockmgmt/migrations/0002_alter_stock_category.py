# Generated by Django 4.0.5 on 2022-06-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
