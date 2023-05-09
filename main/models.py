from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name