# Generated by Django 2.2.13 on 2020-08-25 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
