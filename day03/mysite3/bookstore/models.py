from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField('book name', max_length=50, unique=True, default='')
    pub = models.CharField('publisher', max_length=100, default='')
    price = models.DecimalField('price', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('market price', max_digits=7, decimal_places=2, default=0.0)

    class Meta:
        db_table = 'book'


class Author(models.Model):
    
    name = models.CharField('author name', max_length=11)
    age = models.IntegerField('age', default=1)
    email = models.EmailField('email', null=True)

    class Meta:
        db_table = 'author'