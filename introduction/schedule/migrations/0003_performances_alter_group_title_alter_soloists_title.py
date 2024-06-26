# Generated by Django 4.2.13 on 2024-05-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_soloists'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование номера')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='soloists',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Имя солиста'),
        ),
    ]
