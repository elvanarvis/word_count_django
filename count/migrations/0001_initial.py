# Generated by Django 3.1.4 on 2020-12-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counting_text', models.TextField(max_length=10000, null=True, verbose_name='Enter text')),
                ('result', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]