from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField (max_length= 100 )
    text = models. TextField(null= True,  blank = True)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.title
