from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin, Group


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('У пользователя должен быть email')

        user = self.model(
            username=self.normalize_email(username),
        )
        user.set_password(password)
        user.save()
        # todo Наверняка можно лучше
        user.groups.add(Group.objects.get_or_create(name='Subscriber')[0])
        user.save()
        return user

    def create_superuser(self, username, password=None):

        user = self.create_user(
            username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    USERNAME_FIELD = 'username'
    objects = UserManager()

    username = models.EmailField(
        verbose_name='Email',
        unique=True,
        error_messages={
            'unique': 'Пользователь с таким адресом уже зарегистрирован'
        }
    )
    is_staff = models.BooleanField(
        default=False,
    )

