# Generated by Django 2.1.2 on 2018-10-22 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='B2G',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='b2g',
            name='b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Boy'),
        ),
        migrations.AddField(
            model_name='b2g',
            name='g',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Girl'),
        ),
    ]
