from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # Roles
    ROLE_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("other", "Other"),
    ]

    # Required fields
    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone_number = models.CharField(max_length=25, unique=True, verbose_name="Phone Number")
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")

    # Optional fields
    institution = models.ForeignKey(
        "academia.Institution",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="users",
        verbose_name="Institution",
    )
    major = models.ForeignKey(
        "academia.Subject",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="users",
        verbose_name="Major",
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True,
        verbose_name="Avatar",
    )

    # Role
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")
    is_superuser = models.BooleanField(default=False, verbose_name="Is Superuser")

    # Override AbstractUser defaults
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]

    objects = UserManager()

    # Metaclass
    class Meta:
        verbose_name = "User"  # Singular name in admin panel
        verbose_name_plural = "Users"  # Plural name in admin panel

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
