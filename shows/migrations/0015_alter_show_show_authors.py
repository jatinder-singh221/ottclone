# Generated by Django 3.2.2 on 2021-05-12 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shows', '0014_alter_show_show_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_authors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_related', to=settings.AUTH_USER_MODEL),
        ),
    ]
