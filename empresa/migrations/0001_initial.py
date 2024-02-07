# Generated by Django 5.0.2 on 2024-02-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=100)),
                ('fantasia', models.CharField(max_length=100)),
                ('razao_social', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
    ]
