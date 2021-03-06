# Generated by Django 4.0.4 on 2022-05-18 16:10

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='items.category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('stock_quantity', models.IntegerField()),
                ('dtype', models.CharField(choices=[('BOOK', 'Book'), ('ALBUM', 'Album'), ('MOVIE', 'Movie')], default='BOOK', max_length=16)),
                ('artist', models.CharField(blank=True, max_length=16)),
                ('etc', models.CharField(blank=True, max_length=64)),
                ('author', models.CharField(blank=True, max_length=16)),
                ('isbn', models.CharField(blank=True, max_length=32)),
                ('director', models.CharField(blank=True, max_length=16)),
                ('actor', models.CharField(blank=True, max_length=32)),
                ('categories', models.ManyToManyField(to='items.category')),
            ],
        ),
    ]
