# Generated by Django 4.2.4 on 2023-09-20 15:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0005_alter_reservation_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', ckeditor.fields.RichTextField()),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]