from django.contrib.auth.models import AbstractUser
from django.db import models
from cryptography.fernet import Fernet
from django.utils.timezone import now

# Encryption key for sensitive data
key = Fernet.generate_key()
cipher_suite = Fernet(key)


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('member', 'Member'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    is_verified = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)

    # Add a phone field
    phone = models.CharField(max_length=15, null=True, blank=True)

    encrypted_phone = models.BinaryField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.phone:
            self.encrypted_phone = cipher_suite.encrypt(self.phone.encode())
        super().save(*args, **kwargs)


class Membership(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('inactive', 'Inactive'),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="membership")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    start_date = models.DateField(auto_now_add=True)
    renewal_date = models.DateField(null=True, blank=True)


class Document(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="documents")
    file = models.FileField(upload_to='documents/')
    verified = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class SavingsPlan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="savings")
    plan_name = models.CharField(max_length=100)
    interest_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Contribution(models.Model):
    savings_plan = models.ForeignKey(SavingsPlan, on_delete=models.CASCADE, related_name="contributions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contributed_at = models.DateTimeField(auto_now_add=True)


class AuditLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="audit_logs")
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


class ErrorLog(models.Model):
    error_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
