# Generated by Django 5.2 on 2025-05-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_slug_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='full_description',
            field=models.TextField(null=True),
        ),
    ]
