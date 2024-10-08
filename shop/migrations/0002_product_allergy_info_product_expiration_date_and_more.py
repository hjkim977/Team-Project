# Generated by Django 5.1.1 on 2024-09-09 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='allergy_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='livestock_trace_info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='packaging_type',
            field=models.CharField(default='기본 포장 타입', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='sales_unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(default='기본 판매자', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_info',
            field=models.CharField(default='기본 배송 정보', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='weight_volume',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
