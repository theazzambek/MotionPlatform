from django.contrib.auth.base_user import BaseUserManager


class CustomManager(BaseUserManager):

    def create_user(self, email, firstname, lastname, password, **extra_fields):

        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        user.is_active = True
        return user

    def create_superuser(self, email, firstname, lastname, password, **extra_fields):
        if not email:
            raise ValueError('Email not provided')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            **extra_fields
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_teachers(self):
        from .models import UserType
        return self.get_queryset().filter(role=UserType.TEACHER)

    def get_student(self):
        from .models import UserType
        return self.get_queryset().filter(role=UserType.STUDENT)