# Generated by Django 2.2.13 on 2020-08-27 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_book_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
