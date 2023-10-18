from django.db import models


# Create your models here.
class Cars(models.Model):
    CarName = models.CharField(max_length=255)
    CarModelYear = models.CharField(max_length=255)
    Price = models.CharField(max_length=255)


class SellInsert(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    ModelName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    Location = models.CharField(max_length=255)
    Year = models.IntegerField()

    class Meta:
        db_table = "users"


class buy(models.Model):
    firstname  = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year = models.IntegerField()
    modelname = models.CharField(max_length=255)

    class Meta:
        db_table = "ds"


class cont(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

    class Meta:
        db_table = "contact"
