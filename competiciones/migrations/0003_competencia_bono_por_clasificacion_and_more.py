# Generated by Django 5.1.4 on 2025-01-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competiciones', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competencia',
            name='bono_por_clasificacion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competencia',
            name='bono_por_partido',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competencia',
            name='bono_por_titulo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competencia',
            name='bono_por_victoria',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competencia',
            name='fases',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='competencia',
            name='sistema_puntos',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='competencia',
            name='trofeo',
            field=models.BooleanField(default=True),
        ),
    ]
