# Generated by Django 4.2.7 on 2023-12-10 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_alter_attendance_class_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='date_added',
            new_name='attendance_date',
        ),
    ]