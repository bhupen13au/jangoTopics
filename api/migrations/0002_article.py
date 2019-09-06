# Generated by Django 2.2.3 on 2019-09-06 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('auther', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
            ],
            options={
                'db_table': 'Article',
            },
        ),
    ]
