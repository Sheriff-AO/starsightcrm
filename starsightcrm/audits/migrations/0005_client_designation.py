# Generated by Django 3.1.4 on 2021-01-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0004_client_rep_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='designation',
            field=models.CharField(max_length=200, null=True),
        ),
    ]