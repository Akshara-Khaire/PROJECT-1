from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    Date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',null='True')

    def __str__(self):
        return self.first_name
    

