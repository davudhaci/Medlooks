# Generated by Django 3.0.7 on 2020-06-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorregister',
            name='fax',
            field=models.CharField(default='Qeyd Edilmiyib', max_length=30, verbose_name='Fax'),
        ),
    ]