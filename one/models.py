from django.db import models

# Create your models here.

class log(models.Model):
    tittle = models.CharField(verbose_name='标题',max_length=50,default='')
    text = models.TextField(verbose_name='文章')
    pic = models.ImageField(verbose_name='图片', upload_to='img')
    time = models.DateField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.tittle