from django.db import models

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

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=60)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()


