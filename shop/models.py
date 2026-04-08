from django.db import models

class Order(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name