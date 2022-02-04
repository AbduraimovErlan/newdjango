# Generated by Django 4.0.2 on 2022-02-02 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_users', '0002_customuser_nation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='education',
            field=models.IntegerField(choices=[(1, 'SINGLE'), (2, 'MARRIED'), (3, 'WIDOWED')], null=True, verbose_name='Семейное положение'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='maritalStatus',
            field=models.IntegerField(choices=[(1, 'SINGLE'), (2, 'MARRIED'), (3, 'WIDOWED')], null=True, verbose_name='Семейное положение'),
        ),
    ]