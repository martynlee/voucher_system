from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Voucher(models.Model):
    VOUCHER_TYPE_CHOICES = [
        ('PO', 'Percentage off'),
        ('RO', 'Real Value')
    ]
    code = models.CharField(max_length=10)
    voucher_type = models.CharField(
        max_length=2,
        choices=VOUCHER_TYPE_CHOICES,
        default='PO'
    )
    discount_value = models.IntegerField(validators=[MinValueValidator(0),
                                                    MaxValueValidator(100)])
    # limits = models.IntegerField()
    # active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
