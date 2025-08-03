from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('staff/',views.staff,name='dashboard-staff'),
    path('staff/details/<int:pk>/',views.staff_detail,name='dashboard-staff-detail'),
    path('product/',views.product,name='dashboard-product'),
    path('order/',views.order,name='dashboard-order'),
    path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
     path('product/import/', views.import_products, name='dashboard-product-import'),
    path('product/<str:category>/', views.get_products_for_category, name='dashboard-index'),
    # ...existing code...
   
# ...existing code...
]
