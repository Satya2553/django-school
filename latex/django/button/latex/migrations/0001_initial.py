# Generated by Django 4.1.4 on 2023-01-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plaintext', models.CharField(max_length=500)),
            ],
        ),
    ]
