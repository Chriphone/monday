# Generated by Django 4.1 on 2022-09-09 20:25

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
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=10, null=True)),
                ('date', models.DateField()),
                ('cl', models.CharField(max_length=10)),
                ('present_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('by', models.CharField(default='school', max_length=20, null=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('desscription', models.CharField(max_length=120, verbose_name='desscription')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.PositiveIntegerField()),
                ('joindate', models.DateField(auto_now_add=True)),
                ('mobile', models.CharField(max_length=40)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=40, null=True)),
                ('COURSE', models.CharField(max_length=40, null=True)),
                ('ID_NUMBER', models.CharField(max_length=40, null=True)),
                ('LEVEL', models.CharField(max_length=40, null=True)),
                ('ACADEMIC_YEAR', models.CharField(max_length=40, null=True)),
                ('RESIDENCE', models.CharField(max_length=40, null=True)),
                ('TEL_NO', models.CharField(max_length=40, null=True)),
                ('TEL_NO1', models.CharField(max_length=40, null=True)),
                ('fee', models.PositiveIntegerField(null=True)),
                ('cl', models.CharField(choices=[('ICT', 'ICT'), ('HD', 'HD'), ('TD', 'TD'), ('FB', 'FB')], default='one', max_length=10)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
