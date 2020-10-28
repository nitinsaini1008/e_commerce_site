# Generated by Django 3.1.2 on 2020-10-27 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='buyed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_item', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('desc', models.CharField(max_length=500)),
                ('type_of_item', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='itmephotos')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to='itmephotos')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ManyToManyField(to='pro.items')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ManyToManyField(to='pro.buyed')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='buyed',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.items'),
        ),
    ]
