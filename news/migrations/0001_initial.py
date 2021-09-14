# Generated by Django 3.2.7 on 2021-09-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='', max_length=127)),
                ('title', models.CharField(default='', max_length=127)),
                ('link', models.URLField(default='', max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('amount_of_upvotes', models.PositiveIntegerField(default=0, max_length=127)),
            ],
        ),
    ]
