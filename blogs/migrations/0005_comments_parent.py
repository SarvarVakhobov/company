# Generated by Django 4.0.3 on 2022-03-10 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_remove_blog_tag_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blogs.comments'),
        ),
    ]
