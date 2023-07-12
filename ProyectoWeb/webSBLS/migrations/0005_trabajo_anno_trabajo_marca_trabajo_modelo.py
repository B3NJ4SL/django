# Generated by Django 4.1.5 on 2023-05-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSBLS', '0004_categoria_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='anno',
            field=models.IntegerField(default=2010),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='marca',
            field=models.CharField(default='marca', max_length=50),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='modelo',
            field=models.CharField(default='modelo', max_length=50),
        ),
    ]
