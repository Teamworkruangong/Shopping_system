# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-28 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorname', models.CharField(max_length=10, verbose_name='颜色名称')),
                ('colorurl', models.ImageField(upload_to='color/', verbose_name='颜色图片地址')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=100, verbose_name='商品名称')),
                ('gdesc', models.CharField(max_length=100, verbose_name='商品描述')),
                ('oldprice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='原价')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='现价')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodsapp.Category', verbose_name='类别ID')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdurl', models.ImageField(upload_to='', verbose_name='详情图片地址')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsDetailName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdname', models.CharField(max_length=30, verbose_name='详情名称')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='库存数量')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodsapp.Color')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodsapp.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=10, verbose_name='尺寸名称')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodsapp.Size'),
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='detailname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodsapp.GoodsDetailName'),
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodsapp.Goods'),
        ),
    ]
