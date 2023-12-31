# Generated by Django 3.2.12 on 2023-11-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('pdf', models.FileField(upload_to='book/pdf')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='book/cover')),
            ],
        ),
    ]
