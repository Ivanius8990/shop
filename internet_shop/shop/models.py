from django.db import models


class ShopProducts(models.Model):
    title = models.CharField(max_length=200, verbose_name='название',blank=False)
    content = models.TextField(verbose_name='описание',blank=False)
    photo = models.ImageField(upload_to="img", verbose_name='фото',blank=True)
    prise = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)
    raiting = models.IntegerField(default=5)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    sale = models.IntegerField(default=None)
    new = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'
        ordering = ['id']


class Users(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.CharField(max_length=200, verbose_name='email')


class Basket(models.Model):
    session_key = models.CharField(max_length=255, verbose_name='session_key')
    prod_id = models.IntegerField(verbose_name='id товара')
    numb = models.IntegerField(default=1)
#     products = models.ForeignKey('ShopProducts', on_delete=models.PROTECT)
#     title = models.CharField(max_length=200, verbose_name='название', blank=False)
#     prise_item = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)
#     total_prise = models.FloatField(blank=False,default=None)
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, blank=False)
#     brand = models.ForeignKey('Brand', on_delete=models.PROTECT, blank=False)



    # def __str__(self):
    #     return self.title

    # def save(self, *args, **kwargs):
    #     prise = self.products.prise
    #     print(prise)
    #     self.prise = prise
        # self.total_prise = float(self.prise) * float(self.numb)

        # super(Basket, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
