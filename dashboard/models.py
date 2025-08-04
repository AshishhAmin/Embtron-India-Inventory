from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('Active', (
        ('Transistors', 'Transistors'),
        ('Resistors', 'Resistors'),
        ('Diodes', 'Diodes'),
        ('Microcontrollers', 'Microcontrollers'),
        ('OPAMPS', 'OPAMPS'),
        ('Regulators', 'Regulators'),
        ('Musfets', 'Musfets'),
        ('IGBTS', 'IGBTS'),
        ('BRIDGE Rectifiers', 'BRIDGE Rectifiers'),)),
)
    
class Product(models.Model):
    name = models.CharField(max_length=255 , null=True)
    category = models.CharField(max_length=200, choices=CATEGORY)
    quantity= models.PositiveIntegerField(null=True)
    #price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    location_id = models.CharField(max_length=100, null=True, blank=True)  # Added field
    
    def __str__(self):
        return f'{self.name}-{self.quantity}'
    
    
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User,models.CASCADE,null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    # def total_price(self):
    #     return self.product.price * self.order_quantity if self.product else 0

    # def __str__(self):
    #     return f'{self.product} ordered by {self.staff.username} - Total: ${self.total_price()}'
    
    # def category(self):
    #     return self.product.category if self.product else None