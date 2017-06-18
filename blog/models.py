from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class MyNote(models.Model):
    catagory = models.CharField(max_length=63)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created=models.DateTimeField(default=timezone.now)
    # textfield=models.CharField(max_length=10, default="")

    def __str__(self):
        return self.title


class Device(models.Model):
    DeviceID=models.CharField(max_length=10)
    CustomerProduct=models.CharField(max_length=50)
    Tester=models.CharField(max_length=20, default="")
    NoPara=models.IntegerField(null=True)
    InputDate=models.DateTimeField(default=timezone.now)
    ProductType=models.CharField(max_length=8, null=True)

    def newDevice(self):
        self.InputDate=timezone.now()
        self.save()

    def __str__(self):
        return self.DeviceID
