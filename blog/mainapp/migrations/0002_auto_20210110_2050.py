# Generated by Django 3.1.5 on 2021-01-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='Admin', max_length=100, verbose_name='Автор'),
        ),
    ]