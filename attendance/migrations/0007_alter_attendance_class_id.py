# Generated by Django 4.2.7 on 2023-12-10 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_alter_attendance_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_classId', to='attendance.class'),
        ),
    ]
