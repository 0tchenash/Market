from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from django.utils.translation import gettext_lazy as _


class UserRoles:
    # TODO закончите enum-класс для пользователя
    USER = 'user'
    ADMIN = 'admin'
    ROLE = [(USER, 'Пользователь'), (ADMIN, 'Админ')]


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту


    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    image = models.ImageField(upload_to='user_images/', null=True)
    role = models.CharField(max_length=25, choices=UserRoles.ROLE, default=UserRoles.USER)
    phone = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    objects = UserManager()


    def __str__(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['email']

    def __str__(self):
        return self.email