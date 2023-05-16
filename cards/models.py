from  django.db import models
from django.contrib.auth.models  import User 



STATE_CHOICES=(
    ('Moscow','Procpect Vernadckovo'),
    ('Moscow','university lomovoskov'),
)

CATAGEORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshakk'),
    ('PN','Panner'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
)

class Product(models.Model):
    title =models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATAGEORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title  
    


    
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200) 
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
##__unicode__ is a Python "magic method" that determines how your object looks when you want to display that object as a unicode string. 
# It's not Django-specific or anything, 
# but any time you either call str() or unicode() or use string interpolation and pass that object in, 
# it will call that method to determine what unicode string is returned.