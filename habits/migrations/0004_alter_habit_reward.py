# Generated by Django 4.2.4 on 2023-09-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_options_alter_habit_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='reward',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='награда'),
        ),
    ]
