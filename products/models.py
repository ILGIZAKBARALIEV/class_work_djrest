from django.db import models


class AbstractNameModel(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(AbstractNameModel):
   parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True)


class Tag(AbstractNameModel):
    pass


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null= True,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
    title = models.CharField (max_length= 255 )
    text = models. TextField(null= True,  blank = True)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.title




