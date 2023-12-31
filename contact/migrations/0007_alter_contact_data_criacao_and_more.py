# Generated by Django 4.2.3 on 2023-08-22 11:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_category_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='primeiro_nome',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='show',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telefone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ultimo_nome',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
