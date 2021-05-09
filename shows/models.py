from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .validators import input_validation, image_validation, vedio_validation

class catagories(models.Model):
    catagorie_name = models.CharField('catagorie',max_length=100,validators=[input_validation])

    class Meta:
        db_table = 'catagoires'
        verbose_name_plural = 'catagoires'

    def __str__(self):
        return self.catagorie_name.title()
    
    def get_absolute_url(self):
        return reverse('show:allitems',args=[str(self.catagorie_name)])

class show(models.Model):
    show_authors = models.ForeignKey(User, on_delete = models.CASCADE, null=True,default=1)
    show_name = models.CharField('show name', max_length=100, db_column='show_name',validators=[input_validation])
    show_upload_date = models.DateField(auto_now_add=True,verbose_name='upload date')
    show_title = models.CharField('show title', max_length=100, db_column='show_title',validators=[input_validation])
    show_description = models.CharField('show description', max_length=100, db_column='show_description',validators=[input_validation])
    show_caption = models.ImageField(verbose_name='show caption',upload_to='shows',validators=[image_validation])
    show_catagory = models.ForeignKey(catagories, on_delete=models.CASCADE, verbose_name='catagory', related_name='catagory_related', related_query_name='query_catagory')
    show_vedio = models.FileField(upload_to='vedio',verbose_name='show vedio',validators=[vedio_validation])

    class Meta:
        db_table = 'show_table'
        get_latest_by = ['-show_upload_date']
        verbose_name_plural = 'show'
    
    def __str__(self):
        return self.show_name




