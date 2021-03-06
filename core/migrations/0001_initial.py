# Generated by Django 4.0.2 on 2022-02-17 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categorys',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='items/')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('discounts', models.IntegerField(default=0)),
                ('size', models.CharField(blank=True, choices=[('small', 'Small'), ('medium', 'Medium'), ('full', 'Full')], max_length=50, null=True)),
                ('veg', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.category')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_price', models.IntegerField()),
                ('status', models.CharField(choices=[('received', 'Received'), ('cooking', 'Cooking'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], max_length=50)),
                ('discounts', models.IntegerField(default=0)),
                ('items', models.ManyToManyField(related_name='order', to='core.Item')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.ManyToManyField(related_name='user', to='core.Order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
