# Generated by Django 4.2.4 on 2023-08-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('IT', 'IT'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Medicine', 'Medicine')], max_length=140),
        ),
    ]
