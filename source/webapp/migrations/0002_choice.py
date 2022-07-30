# Generated by Django 4.0.5 on 2022-07-30 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_var', models.TextField(max_length=100, verbose_name='Вариант')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='webapp.polls', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'db_table': 'choices',
            },
        ),
    ]
