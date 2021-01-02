from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    CATEGORY = (
        ('Banking & SMEs', 'Banking & SMEs'),
        ('Commercial & Industries', 'Commercial & Industries'),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    name = models.CharField(max_length=200, null=True)
    rep_name = models.CharField(max_length=200, null=True)
    designation = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, null=True)
    num_of_site = models.IntegerField(null=True)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.category}: {self.name}'