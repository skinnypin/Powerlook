from django.db import models

# Create your models here.
SIZE_CHOICES = [
    ('X', 'Extra Small'),
    ('Sm', 'Small'),
    ('L', 'Large'),
]

class Manproducts(models.Model):
    
    product_name= models.CharField(max_length=255)
    product_price= models.IntegerField()
    product_description= models.TextField()
    product_image = models.ImageField(upload_to='images/')
    product_colour = models.CharField(max_length=100 , null= True, blank= True)
    product_size = models.CharField(max_length= 4 , choices=SIZE_CHOICES, default="Sm")

    
    
    
    def __str__(self):
        return self.product_name
    

class Usermodel(models.Model):
    username = models.CharField( max_length=255)
    email= models.EmailField()
    password= models.CharField( max_length=255)
    
    
class Orderitem(models.Model):
 
    orderitem = models.ForeignKey(Manproducts, on_delete=models.CASCADE)
    
    
class Cart(models.Model):
       ordername = models.ForeignKey(Usermodel, on_delete=models.CASCADE)
       order=models.ForeignKey(Orderitem, on_delete=models.CASCADE)
       
       def __str__(self) -> str:
            return self.ordername.username