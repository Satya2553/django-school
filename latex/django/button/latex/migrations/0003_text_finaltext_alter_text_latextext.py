# Generated by Django 4.1.4 on 2023-01-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0002_text_latextext'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='finaltext',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='text',
            name='latextext',
            field=models.CharField(max_length=100),
        ),
    ]
