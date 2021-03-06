# Generated by Django 3.0.3 on 2020-02-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfolio', '0003_pfolio_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='abouts')),
                ('clients', models.IntegerField(default=0)),
                ('projects', models.IntegerField(default=0)),
                ('collabs', models.IntegerField(default=0)),
            ],
        ),
    ]
