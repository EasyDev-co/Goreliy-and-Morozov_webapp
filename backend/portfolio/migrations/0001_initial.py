# Generated by Django 4.2.1 on 2023-05-24 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('desc', models.TextField(max_length=5000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография кейса')),
                ('case_type', models.CharField(choices=[('B2', 'b2b'), ('EC', 'e_commerce'), ('BT', 'bot')], max_length=2, verbose_name='Тип кейса')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
                'db_table': 'cases',
            },
        ),
        migrations.CreateModel(
            name='Podcasts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('listening_count', models.IntegerField(default=0, verbose_name='Кол-во прослушианий')),
                ('published_at', models.DateTimeField(verbose_name='Дата публикации')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото подкаста')),
            ],
            options={
                'verbose_name': 'Подкаст',
                'verbose_name_plural': 'Подкасты',
                'db_table': 'podcasts',
            },
        ),
        migrations.CreateModel(
            name='PodcastLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=3000, verbose_name='Ссылка на подкаст')),
                ('resource', models.CharField(choices=[('YA', 'yandex'), ('SP', 'spotify'), ('YT', 'youtube')], max_length=2, verbose_name='Ресурс')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcast_link', to='portfolio.podcasts', verbose_name='Подкаст')),
            ],
            options={
                'verbose_name': 'Ссылка на подкаст',
                'verbose_name_plural': 'Ссылки на подкаст',
                'db_table': 'podcasts_links',
            },
        ),
        migrations.CreateModel(
            name='CaseTaskText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.TextField(max_length=5000, verbose_name='Блок текста о задаче кейса')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_task_text', to='portfolio.cases', verbose_name='Блок о кейсе(задача)')),
            ],
            options={
                'verbose_name': 'Блок текста о задаче',
                'verbose_name_plural': 'Блок текста о задаче',
                'db_table': 'cases_task_text',
            },
        ),
        migrations.CreateModel(
            name='CaseResultText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_text', models.TextField(max_length=5000, verbose_name='Блок текста о результате кейса')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_result_text', to='portfolio.cases', verbose_name='Блок о кейсе(результат)')),
            ],
            options={
                'verbose_name': 'Блок текста о результате',
                'verbose_name_plural': 'Блок текста о результате',
                'db_table': 'cases_result_text',
            },
        ),
    ]
