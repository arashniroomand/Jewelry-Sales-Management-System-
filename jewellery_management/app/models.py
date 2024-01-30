from django.db import models
from django.contrib.auth.models import AbstractUser

from users.models import Seller


class Store(models.Model):
    name = models.CharField(max_length=256)
    address = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class StoreSeller(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store}-{self.seller.first_name} {self.seller.last_name}"


class StorePhoneNumber(models.Model):
    phone_number = models.CharField(max_length=13)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store}-{self.phone_number}"


class Jewellery(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=1000)
    quantity = models.PositiveSmallIntegerField()
    mass = models.FloatField()
    wage = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.category}"


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=256)
    address = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class SupplierPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=13)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.supplier}-{self.phone_number}"


class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"


class CustomerPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=13)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer}-{self.phone_number}"


class Order(models.Model):
    jewellery = models.ForeignKey(Jewellery, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer}-{self.jewellery}"


class Payment(models.Model):
    STATUS_CHOICES = [('P', 'Pending'), ('S', 'Successful'), ('D', 'Dismissed')]
    status = models.CharField(choices=STATUS_CHOICES, default='P', max_length=1)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.store}-{self.status}"
