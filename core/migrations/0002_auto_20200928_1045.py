# Generated by Django 3.1.1 on 2020-09-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='category',
            field=models.CharField(choices=[('PROCURA-SE', 'Procura-se'), ('POCRIAÇÃO', 'Pocriação'), ('ADOÇÃO', 'Adoção')], default='PROCURA-SE', max_length=11),
        ),
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(upload_to='pet'),
        ),
    ]
