# Generated by Django 3.1.1 on 2020-10-10 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DasherApp', '0002_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('LOW', 'LOW')], max_length=20, null=True),
        ),
    ]
