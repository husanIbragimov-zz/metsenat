from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if phone is None:
            raise TypeError('Phone did not come')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(phone, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_sponsor = True
        user.is_active = True
        user.save(using=self._db)
        return user


GENDER = (
    (0, "None"),
    (1, "Male"),
    (2, "Female"),
)


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "1. Account"

    full_name = models.CharField(max_length=50, verbose_name="Ism Familiya")
    phone = models.CharField(max_length=13, unique=True, db_index=True, verbose_name="Telefon nomer",
                             help_text="(+998332150548)")
    gender = models.IntegerField(choices=GENDER, default=0, verbose_name="Jinsi")
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser")
    is_staff = models.BooleanField(default=False, verbose_name="Admin")
    is_physical_person = models.BooleanField(default=False, verbose_name="Jismoniy shaxs")
    is_legal_entity = models.BooleanField(default=False, verbose_name="Yuridik shaxs")
    is_sponsor = models.BooleanField(default=False, verbose_name="Xomiy")
    is_student = models.BooleanField(default=False, verbose_name="Talaba")
    is_active = models.BooleanField(default=True)
    date_login = models.DateTimeField(auto_now=True, verbose_name='Yangilangan sanasi')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sanasi')

    objects = AccountManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    @property
    def get_physical_person_count(self):
        user = Account.objects.filter(is_physical_person=True).count()
        return user

    @property
    def get_legal_entity_count(self):
        user = Account.objects.filter(is_legal_entity=True).count()
        return user

    def get_student_count(self):
        user = Account.objects.filter(is_student=True).count()
        return user

    @property
    def token(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data
