# Generated by Django 4.0.1 on 2022-01-25 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pais.pais')),
            ],
        ),
    ]
