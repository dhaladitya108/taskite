import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from taskite.models.base import BaseUUIDTimestampModel


class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name, password=None):
        user = self.model(
            username=username, email=self.normalize_email(email), full_name=full_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name, password):
        user = self.create_user(username, email, full_name, password)
        user.role = "admin"
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(BaseUUIDTimestampModel, AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = ("admin", "Admin")
        STAFF = ("staff", "Staff")
        GUEST = ("guest", "Guest")

    username = models.CharField(max_length=124, unique=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STAFF)
    avatar = models.ImageField(blank=True, null=True, upload_to="users/avatars/")

    display_name = models.CharField(max_length=125, blank=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "full_name"]

    class Meta:
        db_table = "users"
        ordering = ("-created_at",)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.display_name:
                self.display_name = self.full_name.split()[0].lower()

            if not self.username:
                self.username = f"{self.display_name}{random.randint(1, 100)}"
        return super().save(*args, **kwargs)
