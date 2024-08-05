import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager


class Rename:
    def __init__(self, path):
        self.path = path

    def rename(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), ext)
        return os.path.join(self.path, filename)


class UserType(models.IntegerChoices):
    TEACHER = 1, "УЧИТЕЛЬ"
    STUDENT = 2, "СТУДЕНТ"


class MyUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    username = None
    first_name = None
    last_name = None
    # last_login = None

    role = models.PositiveSmallIntegerField(
        choices=UserType.choices,
        default=UserType.STUDENT,
        verbose_name="Тип пользователя"
    )
    uniqueId = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(
        max_length=125,
        verbose_name='Имя'
    )
    lastname = models.CharField(
        max_length=125,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    speciality = models.CharField(
        max_length=125,
        verbose_name='Специальность'
    )
    experience = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Опыт работы (лет)'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name="Админ"
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = CustomManager()

    @property
    def is_staff(self):
        return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self.is_admin = value

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(MyUser, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
