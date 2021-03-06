# Generated by Django 4.0.2 on 2022-02-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eClass7_1_CC_en_01_190102xx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Supplier', models.CharField(max_length=6)),
                ('IdCC', models.CharField(max_length=9)),
                ('Identifier', models.CharField(max_length=6)),
                ('VersionNumber', models.FloatField()),
                ('RevisionNumber', models.FloatField()),
                ('ISOLanguageCode', models.CharField(max_length=2)),
                ('ISOCountryCode', models.CharField(max_length=2)),
                ('IrdiCC', models.CharField(max_length=20)),
            ],
        ),
    ]
