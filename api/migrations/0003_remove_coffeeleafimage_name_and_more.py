# Generated by Django 5.1.4 on 2024-12-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_coffeeleafimage_delete_fruitimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeeleafimage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='coffeeleafimage',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='coffeeleafimage',
            name='label',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coffeeleafimage',
            name='image',
            field=models.ImageField(upload_to='coffee_leaf_images/'),
        ),
    ]
