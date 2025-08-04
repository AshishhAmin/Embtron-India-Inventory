from django import forms
from .models import Product, Order

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity','location_id']

class OrderForm(forms.ModelForm):
    # We define the category field as a ChoiceField to allow selection of categories
    CATEGORY = (
    ('Active', (
        ('Transistors', 'Transistors'),
        ('Resistor', 'Resistor'),
        ('Diodes', 'Diodes'),
        ('Microcontrollers', 'Microcontrollers'),
        ('OPAMPS', 'OPAMPS'),
        ('Regulators', 'Regulators'),
        ('Musfets', 'Musfets'),
        ('IGBTS', 'IGBTS'),
        ('BRIDGE Rectifiers', 'BRIDGE Rectifiers'),)),
    ('Electronics', (
        ('Computers', 'Computers'),
        ('Mobile Phones', 'Mobile Phones'),
        ('Accessories', 'Accessories'),
    )),
    ('Food', (
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Snacks', 'Snacks'),
    )),
)
    category = forms.ChoiceField(choices=CATEGORY, required=True)
    
    # The product field is a ModelChoiceField, but we'll filter it dynamically with JavaScript
    
    product = forms.ModelChoiceField(queryset=Product.objects.none(), required=True)
    
    class Meta:
        model = Order
        fields = ['category', 'product', 'order_quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initially, the 'product' field will have no products
        self.fields['product'].queryset = Product.objects.all()