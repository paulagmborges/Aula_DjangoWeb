# Generated by Django 4.2.10 on 2024-03-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('Iniciante', 'Iniciante'), ('Intermediario', 'Intermediario'), ('Avançado', 'Avaçado')], max_length=50),
        ),
    ]