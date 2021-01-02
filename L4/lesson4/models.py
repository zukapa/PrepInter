from django.db import models


class Products(models.Model):
    name = models.CharField(verbose_name=u'Наименование товара',
                            max_length=255)
    date_rec = models.DateField(verbose_name=u'Дата поступления')
    price = models.PositiveIntegerField(verbose_name=u'Цена', default=0)
    u_measure = models.CharField(verbose_name=u'Единица измерения',
                                 max_length=30)
    name_provider = models.CharField(verbose_name=u'Поставщик',
                                     max_length=255)

    def __unicode__(self):
        return self.name
