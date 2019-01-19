# Generated by Django 2.0.3 on 2018-10-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createArrangement', '0008_auto_20181003_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classrooms',
            name='cols',
        ),
        migrations.RemoveField(
            model_name='classrooms',
            name='roomid',
        ),
        migrations.RemoveField(
            model_name='classrooms',
            name='rows',
        ),
        migrations.RemoveField(
            model_name='deptandsec',
            name='endingRoll',
        ),
        migrations.RemoveField(
            model_name='deptandsec',
            name='nameOfDept',
        ),
        migrations.RemoveField(
            model_name='deptandsec',
            name='secCapacity',
        ),
        migrations.RemoveField(
            model_name='deptandsec',
            name='secName',
        ),
        migrations.RemoveField(
            model_name='deptandsec',
            name='sectionsInDept',
        ),
        migrations.RemoveField(
            model_name='deptandsec',
            name='startingRoll',
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room1',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room10',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room2',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room3',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room4',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room5',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room6',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room7',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room8',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='room9',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section1',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section10',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section2',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section3',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section4',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section5',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section6',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section7',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section8',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='deptandsec',
            name='section9',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]