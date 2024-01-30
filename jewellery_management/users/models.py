from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class SellerManager(BaseUserManager):
    def create_user(self, permission_id, password=None):
        user = self.model(permission_id=permission_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, permission_id, password=None):
        user = self.create_user(permission_id, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Seller(AbstractBaseUser, PermissionsMixin):
    permission_id = models.CharField(max_length=10, unique=True, primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = SellerManager()

    USERNAME_FIELD = 'permission_id'

    def __str__(self):
        return self.permission_id

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class SellerPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=13)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.phone_number}-{self.seller.permission_id}"
