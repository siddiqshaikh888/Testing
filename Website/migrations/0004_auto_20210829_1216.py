# Generated by Django 3.2.6 on 2021-08-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_auto_20210827_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='websitedetail',
        ),
    ]
