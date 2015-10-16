# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coursetracer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TermCode', models.IntegerField()),
                ('TermDistr', models.CharField(max_length=100)),
                ('crn', models.IntegerField()),
                ('subj', models.CharField(max_length=3)),
                ('courseNum', models.IntegerField()),
                ('sect', models.IntegerField()),
                ('scheDesc', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('maxEnroll', models.IntegerField()),
                ('actEnroll', models.IntegerField()),
            ],
        ),
    ]
