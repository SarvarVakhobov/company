# Generated by Django 4.0.3 on 2022-03-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_custom_user_category_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_worker',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
