# Generated by Django 2.1.7 on 2019-04-09 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer', models.IntegerField()),
                ('positiveInteger', models.PositiveIntegerField()),
                ('positiveSmallInteger', models.PositiveSmallIntegerField()),
                ('bigInteger', models.BigIntegerField()),
                ('floatt', models.FloatField()),
                ('binary', models.BinaryField()),
                ('boolean', models.BooleanField()),
                ('char', models.CharField(max_length=5)),
                ('text', models.TextField(max_length=20)),
                ('data', models.DateField()),
                ('dataTime', models.DateTimeField()),
                ('decimal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('email', models.EmailField(max_length=254)),
                ('filee', models.FileField(upload_to='')),
                ('imagee', models.ImageField(upload_to='')),
            ],
        ),
    ]
