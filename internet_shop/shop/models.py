from django.db import models

class ShopProducts(models.Model):
    title = models.CharField(max_length=200,verbose_name='название')
    content = models.TextField(blank=False,verbose_name='описание')
    photo = models.ImageField(upload_to="img",verbose_name='фото')
    prise = models.FloatField()
    raiting = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True,verbose_name='опубликовано')
    sale = models.IntegerField(default=None)
    new = models.BooleanField(default=True)
    cat = models.ForeignKey('Category',on_delete=models.PROTECT)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True,verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



class Brand(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name



class Users(models.Model):
    first_name = models.CharField(max_length=200,verbose_name='Имя')
    last_name = models.CharField(max_length=200,verbose_name='Фамилия')
    email = models.CharField(max_length=200, verbose_name='email')
