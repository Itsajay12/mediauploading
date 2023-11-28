from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField( max_length=50)
    pdf=models.FileField( upload_to='book/pdf')
    cover=models.ImageField( upload_to='book/cover',null=True,blank=True )