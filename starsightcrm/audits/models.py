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
        return f'{self.name}'

class Site(models.Model):
    STATUS = (
        ('Scheduled for Audit', 'Scheduled for Audit'),
        ('Scheduled for Data-logging', 'Scheduled for Data-logging'),
        ('Scheduled for Audit & Data-logging', 'Scheduled for Audit & Data-logging'),
        ('Pending Schedule', 'Pending Schedule'),
        ('Audited', 'Audited'),
        ('Data-logged', 'Data-logged'),
        ('Audited & Data-logged', 'Audited & Data-logged'),
    )
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    branch = models.CharField(max_length=50, null=True)
    address = models.TextField(max_length =200, null=True)
    state = models.CharField(max_length=20, null=True)
    region = models.CharField(max_length=4, null=True)
    contact_person = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact_num = models.CharField(max_length=16, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    date_recv = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.client} - {self.branch}'


class Vendor(models.Model):
    site = models.ManyToManyField(Site, null=True)
    name = models.CharField(max_length=100, null=True)
    rep_name = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=16, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.name

