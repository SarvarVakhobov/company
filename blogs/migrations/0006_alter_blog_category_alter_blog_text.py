# Generated by Django 4.0.3 on 2022-03-15 12:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_comments_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog', to='blogs.category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]