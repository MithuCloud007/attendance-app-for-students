# Generated by Django 4.2.7 on 2023-12-07 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_alter_department_status'),
        ('attendance', '0002_alter_attendance_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_studentId', to='department.department'),
        ),
    ]