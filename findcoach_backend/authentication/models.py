# Create your models here.
# customise user model
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# User = get_user_model()


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email.split('@')[0]

    def get_short_name(self):
        return self.email.split('@')[0]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    price = models.IntegerField()
    category = models.CharField(max_length=30, blank=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=30, blank=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.user.username


class CoachClient(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField(max_length=500, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.coach.user.username + " " + self.client.user.username


class CoachCategory(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.coach.user.username + " " + self.category


class ClientCategory(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.client.user.username + " " + self.category


class CoachAvailability(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.coach.user.username + " " + self.date + " " + self.time


class CoachSchedule(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.coach.user.username + " " + self.client.user.username + " " + self.date + " " + self.time


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " " + self.content