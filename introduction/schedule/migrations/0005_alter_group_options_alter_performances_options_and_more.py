# Generated by Django 4.2.13 on 2024-05-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_schedules'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name'], 'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='performances',
            options={'ordering': ['title'], 'verbose_name': 'Выступление', 'verbose_name_plural': 'Выступления'},
        ),
        migrations.AlterModelOptions(
            name='soloists',
            options={'ordering': ['name'], 'verbose_name': 'Солист', 'verbose_name_plural': 'Солисты'},
        ),
        migrations.RenameField(
            model_name='group',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='soloists',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='schedules',
            name='group_2',
            field=models.ManyToManyField(related_name='schedules_2', to='schedule.group', verbose_name='Группы 2'),
        ),
        migrations.AlterField(
            model_name='performances',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название выступления'),
        ),
        migrations.RemoveField(
            model_name='schedules',
            name='group',
        ),
        migrations.AlterField(
            model_name='schedules',
            name='number',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'), (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'), (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'), (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'), (90, '90'), (91, '91'), (92, '92'), (93, '93'), (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99')], verbose_name='Номер по порядку'),
        ),
        migrations.RemoveField(
            model_name='schedules',
            name='solist',
        ),
        migrations.AddField(
            model_name='schedules',
            name='group',
            field=models.ManyToManyField(related_name='schedules', to='schedule.group', verbose_name='Группы'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='solist',
            field=models.ManyToManyField(related_name='schedules', to='schedule.soloists', verbose_name='Солисты'),
        ),
    ]
