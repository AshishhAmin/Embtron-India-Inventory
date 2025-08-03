from django.shortcuts import render,redirect
from .models import Product,Order
from django.contrib.auth.decorators import login_required
from .forms import ProductForm,OrderForm,CsvImportForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import Product
from django.db.models import Sum

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count=orders.count()
    product_count=products.count()
    workers_count = User.objects.all().count()

    # Calculate sales for each product
    products_with_sales = []
    for product in products:
        sales = Order.objects.filter(product=product).aggregate(total_sales=Sum('order_quantity'))['total_sales'] or 0
        products_with_sales.append({
            'name': product.name,
            'quantity': product.quantity,
            'sales': sales,
            'price': product.price,
            'category': product.category.name if hasattr(product.category, 'name') else product.category  # Add this line
        })

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            
            # Get the product associated with the order
            product = instance.product
            
            # Check if there is enough stock
            if product.quantity >= instance.order_quantity:
                # Save the order
                instance.save()
                
                # Update the product quantity
                product.quantity -= instance.order_quantity
                product.save()  # Save the updated product
                
                messages.success(request, f'Order for {instance.order_quantity} of {product.name} has been placed.')
                
            else:
                messages.error(request, f'Not enough stock available for this product.')
            
    else:
        products = Product.objects.all()
        form = OrderForm()
    
    context = {
        'orders': orders,
        'form': form,
        'products':products_with_sales,
        'orders_count':orders_count,
        'product_count':product_count,
        'workers_count':workers_count,
        
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count=workers.count()
    orders = Order.objects.all()
    orders_count= orders.count()
    product_count = Product.objects.all().count()
    context={
        'workers':workers,
        'workers_count': workers_count,
        'orders_count':orders_count,
        'product_count':product_count
    }
    return render(request,'dashboard/staff.html',context)

def staff_detail(request,pk):
    workers=User.objects.get(id=pk)
    context={
        'worker':workers,
    }
    return render(request,'dashboard/staff_detail.html',context)

@login_required(login_url='user-login')
def product(request):
    items =Product.objects.all()
    product_count=items.count()
    #items=Product.objects.raw('SELECT * FROM dashboard_product')
    workers_count = User.objects.all().count()
    orders = Order.objects.all()
    orders_count= orders.count()
    if request.method =='POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name =form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context ={
        'items':items,
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count
    }
    return render(request,'dashboard/product.html',context)

def product_delete(request,pk):
    item =Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

def product_update(request, pk):
    item= Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form=ProductForm(instance=item)


    context={
        'form':form,

    }
    return render(request,'dashboard/product_update.html',context)


@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count=orders.count()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    context={
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count
    }
    return render(request,'dashboard/order.html',context)


def get_products_for_category(request, category):
    # Filter products by the selected category
    products = Product.objects.filter(category=category)
    # Create a list of product dictionaries to send as JSON
    product_data = [{'id': product.id, 'name': product.name} for product in products]
    
    return JsonResponse({'products': product_data})

import csv
from io import TextIOWrapper
from django.contrib import messages

@login_required(login_url='user-login')
def import_products(request):
    if request.method == 'POST':
        form = CsvImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='utf-8')
            reader = csv.DictReader(csv_file)
            for row in reader:
                Product.objects.create(
                    name=row['name'],
                    category=row['category'],
                    quantity=row['quantity'],
                    price=row['price'],
                    location_id=row.get('location_id', '')
                )
            messages.success(request, 'Products imported successfully!')
            return redirect('dashboard-product')
    else:
        form = CsvImportForm()
    return render(request, 'dashboard/import_products.html', {'form': form})