# Generated by Django 4.0.4 on 2022-06-18 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': ' users'},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
