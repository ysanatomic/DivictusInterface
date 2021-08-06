# Generated by Django 3.2.5 on 2021-08-06 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0008_notes_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPCPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('last_online', models.DateTimeField(null=True)),
                ('is_currently_online', models.BooleanField(default=False)),
            ],
        ),
    ]
