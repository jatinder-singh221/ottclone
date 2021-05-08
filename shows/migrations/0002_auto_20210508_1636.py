# Generated by Django 3.2.2 on 2021-05-08 11:06

from django.db import migrations, models
import django.db.models.deletion
import shows.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagories',
            name='catagorie_name',
            field=models.CharField(max_length=100, validators=[shows.validators.input_validation], verbose_name='catagorie'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_caption',
            field=models.ImageField(upload_to='shows', validators=[shows.validators.image_validation], verbose_name='show caption'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catagory_related', related_query_name='query_catagory', to='shows.catagories', verbose_name='catagory'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_description',
            field=models.CharField(db_column='show_description', max_length=100, validators=[shows.validators.input_validation], verbose_name='show description'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_name',
            field=models.CharField(db_column='show_name', max_length=100, validators=[shows.validators.input_validation], verbose_name='show name'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_title',
            field=models.CharField(db_column='show_title', max_length=100, validators=[shows.validators.input_validation], verbose_name='show title'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_vedio',
            field=models.FileField(upload_to='vedio', validators=[shows.validators.vedio_validation], verbose_name='show vedio'),
        ),
    ]