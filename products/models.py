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

    @property
    def tag_names(self):
        return [i.name for i in self.tags.all()]



STARS = (
    (star,'*'* star) for star in range(1,6)
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STARS, default=5)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text
