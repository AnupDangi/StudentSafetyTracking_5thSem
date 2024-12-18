from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.timezone import localtime

class StudentManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and returns a regular user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with an email, password, and all privileges.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        # Provide default values for required fields for the superuser
        extra_fields.setdefault("full_name", "Admin")
        extra_fields.setdefault("age", 30)  # Default age for the superuser
        extra_fields.setdefault("nationality", "N/A")
        extra_fields.setdefault("college", "N/A")
        extra_fields.setdefault("college_address", "N/A")
        extra_fields.setdefault("city", "N/A")
        extra_fields.setdefault("location_consent", True)

        return self.create_user(email, password, **extra_fields)


class Student(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)  # Allow null and blank for age
    nationality = models.CharField(max_length=100, blank=True, default="")
    college = models.CharField(max_length=100, blank=True, default="")
    college_address = models.CharField(max_length=255, blank=True, default="")
    city = models.CharField(max_length=100, blank=True, default="")
    location_consent = models.BooleanField(default=False)

    # Authentication fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = StudentManager()

    class Meta:
        db_table = 'student'  # Explicitly set the table name for Student

    def __str__(self):
        return self.email


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=localtime)

    class Meta:
        db_table = 'attendance'  # Explicitly set the table name for Attendance
        unique_together = ('student', 'timestamp')
        verbose_name_plural = "Attendances"
        ordering = ['-timestamp'] 

    def __str__(self):
        return f"{self.student.full_name} - {self.timestamp}"

