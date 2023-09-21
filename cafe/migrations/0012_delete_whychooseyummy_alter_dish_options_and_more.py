# Generated by Django 4.2.4 on 2023-09-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0011_remove_whychooseyummy_icon_boxes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WhyChooseYummy',
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('category', 'position'), 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AlterUniqueTogether(
            name='dish',
            unique_together={('id', 'slug')},
        ),
        migrations.AddConstraint(
            model_name='dish',
            constraint=models.UniqueConstraint(fields=('position', 'category'), name='unique_position_per_category'),
        ),
    ]