from django.contrib import admin
from .models import Manproducts, Usermodel, Orderitem, Cart
# Register your models here.
admin.site.register(Manproducts)
admin.site.register(Usermodel)
admin.site.register(Orderitem)
admin.site.register(Cart)