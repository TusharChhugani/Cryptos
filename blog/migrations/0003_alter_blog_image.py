# Generated by Django 3.2.10 on 2021-12-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='blogindex.jpg', null=True, upload_to='blog-pics'),
        ),
    ]
