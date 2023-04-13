from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'
    
class Quote(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE,)
    text = models.CharField(max_length=2000, null=False, unique=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f'{self.text}'

class Author(models.Model):
    fullname = models.CharField(max_length=25, null=False, unique=True)
    born_date = models.CharField(max_length=25, null=False)
    born_location = models.CharField(max_length=25, null=False)
    description = models.CharField(max_length=5000, null=False, unique=True)

    def __str__(self):
        return f'{self.fullname}'