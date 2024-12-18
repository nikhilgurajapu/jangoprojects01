from django.db import models

class martprices(models.Model):
    costomername = models.CharField(max_length=100)
    product_1 = models.IntegerField()
    product_2 = models.IntegerField()
    product_3 = models.IntegerField()
    product_4 = models.IntegerField()
    product_5 = models.IntegerField()
    product_6 = models.IntegerField()
    product_7 = models.IntegerField()
