from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)


# customer registration
class Register(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name

#     add work for worker in admin_base
class work(models.Model):
    name=models.CharField(max_length=100)
    charge=models.IntegerField()

    # for returning only the name in model work
    def __str__(self):
        return self.name

class worker_register(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_pic=models.FileField(upload_to='profilepic/')
    address = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=40)
    email = models.EmailField()
    work_type=models.ForeignKey(work,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class complaints(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True,blank=True)

class schedule(models.Model):
    worker =models.ForeignKey(worker_register,on_delete=models.CASCADE)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()

# take appoinments by customer


class take_appoinments(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE)
    schedule=models.ForeignKey(schedule,on_delete=models.CASCADE)
    status =models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)





class Bill(models.Model):
    name=models.ForeignKey(Register,on_delete=models.CASCADE)
    bill_date=models.DateTimeField(auto_now_add=True)
    amount=models.IntegerField()
    paid_on=models.DateField(auto_now=True)
    status=models.IntegerField(default=0)


class CreditCard(models.Model):
    name = models.ForeignKey(Register, on_delete=models.CASCADE)
    card_no=models.CharField(max_length=30)
    card_cvv=models.CharField(max_length=30)
    expiry_date=models.CharField(max_length=200)

