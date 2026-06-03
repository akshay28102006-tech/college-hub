from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('AIDS', 'AI & DS'),
        ('MECH', 'Mechanical'),
        ('CIVIL', 'Civil'),
        ('ELECTRICAL', 'Electrical'),
        ('ETC', 'Electronics'),
    ]

    full_name = models.CharField(max_length=150)

    profile_photo = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    branch = models.CharField(
        max_length=20,
        choices=BRANCH_CHOICES,
        blank=True
    )

    semester = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.username