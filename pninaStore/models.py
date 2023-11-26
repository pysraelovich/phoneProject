from django.db import models


class Category(models.Model):
    category_name = models.CharField(verbose_name='שם קטגוריה', max_length=50)

    class Meta:
        verbose_name = 'קטגוריה'
        verbose_name_plural = 'קטגוריות'


class Product(models.Model):
    product_name = models.CharField(verbose_name='שם מוצר', max_length=50)
    barcode = models.CharField(verbose_name='ברקוד', max_length=255, unique=True)
    price = models.FloatField(verbose_name='מחיר', default=0.1)
    quantity = models.IntegerField(verbose_name='כמות', default=0)
    category = models.CharField(verbose_name='שם קטגוריה', max_length=50)

    class Meta:
        verbose_name = 'מוצר'
        verbose_name_plural = 'מוצרים'


class Supplier(models.Model):
    supplier_name = models.CharField(verbose_name='שם ספק', max_length=50)
    supplier_phone = models.CharField(verbose_name='טלפון', max_length=10)
    supplier_email = models.EmailField(verbose_name='אימייל')

    class Meta:
        verbose_name = 'ספק'
        verbose_name_plural = 'ספקים'


class Order(models.Model):
    product_name = models.CharField(verbose_name='שם מוצר', max_length=50)
    quantity = models.IntegerField(verbose_name='כמות', default=1)
    supplier_name = models.CharField(verbose_name='שם ספק', max_length=50)
    date = models.DateTimeField(verbose_name='תאריך', auto_now_add=True)

    class Meta:
        verbose_name = 'הזמנה'
        verbose_name_plural = 'הזמנות'

