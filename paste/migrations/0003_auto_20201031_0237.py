# Generated by Django 3.1.2 on 2020-10-31 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0002_auto_20201028_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textfile',
            options={'ordering': ('-time',)},
        ),
        migrations.AddField(
            model_name='textfile',
            name='time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
