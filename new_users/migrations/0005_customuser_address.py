# Generated by Django 4.0.2 on 2022-02-02 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_users', '0004_alter_customuser_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
