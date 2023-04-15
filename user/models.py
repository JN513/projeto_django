from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils.translation import ugettext as _
from django.contrib import auth
from django.core.mail import send_mail

class UserManager(BaseUserManager):
    use_in_migrations = True

    def __create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email não fornecido")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.__db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self.__create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff precisa ser verdadeiro")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser precisa ser verdadeiro")
        
        return self.__create_user(email, password, **extra_fields)
        

    def with_perm(self, perm, is_active=True, incrude_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)

            if len(backend) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError("Mais de um backend de autenticacao fornecido")
            
        


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True, error_messages={
        "unique": "Usuario com esse email já existente"
    })
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    avatar = models.FileField()
    abstract = models.TextField()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "user"
        verbose_name_plurar = "users"

    def __str__ (self):
        return self.first_name
    
    def clean(self):
        super().clean()

        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

