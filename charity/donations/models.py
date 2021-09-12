from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=120)

class Institution(models.Model):
    TYPE = (
        (1, 'Fundacja'),
        (2, 'Organizacja Pozarządowa'),
        (3, 'Zbiórka lokalna'),
    )

    name = models.CharField(max_length=240)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=120, null=True)
    phone_number = models.IntegerField(null=True)
    city = models.CharField(max_length=60, null=True)
    zip_code = models.CharField(max_length=6, null=True)
    pick_up_date = models.DateField(null=True)
    pick_up_time = models.TimeField(null=True)
    pick_up_comment = models.TextField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, default=None)


