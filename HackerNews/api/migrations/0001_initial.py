# Generated by Django 4.0.3 on 2022-03-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
