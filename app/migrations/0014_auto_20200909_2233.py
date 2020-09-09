# Generated by Django 2.2.12 on 2020-09-09 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200902_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='案件カテゴリ')),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='work_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='app.WorkCategory', verbose_name='案件カテゴリ'),
            preserve_default=False,
        ),
    ]
