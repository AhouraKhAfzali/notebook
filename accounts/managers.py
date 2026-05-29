from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
    Custom manager for User model.
    Uses user_name as the username field.
    """

    def create_user(self, email, phone_number, first_name, last_name, password=None, role="student", **extra_fields):
        """
        Create and save a regular user with the given email, phone, first name, last name and role.
        """

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            role=role,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        """
        Create and save a superuser with the given national ID, email, phone, first name and last name.
        """

        user = self.create_user(
            email=email,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role="admin",
            **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
