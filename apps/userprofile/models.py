from django.db import models
from django.contrib.auth import get_user_model


MyUser = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE
    )
    cover = models.ImageField(
        upload_to='covers/',
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        firstname = self.user.firstname if self.user.firstname else "Нет адреса"
        lastname = self.user.lastname if self.user.lastname else "Нет email"
        email = self.user.email if self.user.email else "Нет телефона"
        speciality = self.user.speciality if self.user.speciality else "Нет телефона"
        return f'Имя: {firstname}{lastname}, Email: {email}, Адрес: {speciality}'

