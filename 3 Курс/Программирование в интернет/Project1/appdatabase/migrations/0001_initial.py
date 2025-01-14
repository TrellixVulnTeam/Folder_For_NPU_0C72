# Generated by Django 2.1.7 on 2019-04-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Surname', models.CharField(max_length=150)),
                ('Birth', models.DateField()),
                ('Company', models.CharField(choices=[('DataArt', 'DataArt'), ('EPAM', 'EPAM'), ('DiceUS', 'DiceUS'), ('SoftServe', 'SoftServe'), ('GlobalLogic', 'GlobalLogic')], max_length=150)),
                ('Position', models.CharField(choices=[('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], max_length=15)),
                ('Language', models.CharField(choices=[('C#', 'C#'), ('CPP', 'C++'), ('Python', 'DiceUS'), ('JS', 'JavaScript'), ('PHP', 'PHP')], default=('CPP', 'C++'), max_length=10)),
                ('Salary', models.IntegerField()),
            ],
        ),
    ]
