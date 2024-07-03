from django.shortcuts import render, HttpResponse, redirect
from .models import Manproducts, Usermodel , Cart, Orderitem
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404

#create your views here

from .models import Manproducts  # Import your model here

def index(request):
    data = Manproducts.objects.all()
    print(data)
    return render(request, "index.html", {"mess": "my name is Dhawal", "data": data})


def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('view_cart')




def product(request):
    if request.method == "POST":
        price_range = request.POST.get('price_range')
        size = request.POST.get('size')
        color = request.POST.get('color')
        print("this is my color" , color)
        filters = {}

        if price_range:
            price_min, price_max = map(int, price_range.split('-'))
            filters['product_price__gte'] = price_min
            filters['product_price__lte'] = price_max

        if size:
            filters['product_size'] = size

        
        
        if color :
            filters['product_colour'] = color
        data = Manproducts.objects.filter(**filters)  
    else:
        data = Manproducts.objects.all()

    return render(request, "product.html", {'data': data})
    

   
   # return HttpResponse("This is home page")
def add_cart(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        print(item_id)  # Debug print to ensure item ID is captured

        # Fetch the user with username 'admin'
        try:
            user = Usermodel.objects.get(username='admin')
            print(user, 'logged in user')
        except Usermodel.DoesNotExist:
            # Handle the case where the user does not exist
            print('User with username "admin" does not exist.')
            return redirect('product')  # Or another appropriate view

        try:
            product = Manproducts.objects.get(id=item_id)
        except Manproducts.DoesNotExist:
            # Handle the case where the product does not exist
            return redirect('product')  # Or another appropriate view

        order_item, created = Orderitem.objects.get_or_create(orderitem=product)

        Cart.objects.create(ordername=user, order=order_item)
        return redirect('product')  # Redirect to a relevant view
    else:
        return redirect('product') 
def about(request):
    return HttpResponse("This is about page")

def store(request):
    return render(request, "store.html")

def order(request):
    return render(request,"order.html" )

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = Usermodel.objects.get(username=username)
        password = Usermodel.objects.filter(password= password).exists
        print(user)
        if not user:
            return render(request, "login.html", {'message': 'User doesnt exist signup pls or password is incorrect maybe'})
        
        if not password:
            return render(request, "login.html", {'message' : 'Password is incorrect'}) 
        else:
            return redirect("/",{"user": user.username})
      
    return render(request , "login.html")

def signup(request):
    if request.method == "POST":
        print(request.POST)
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        confirm_password  = request.POST.get('confirmPassword')
        user = Usermodel.objects.filter(username=username).exists
        if not user:
            return render(request, "signup.html", {'message' : 'User already Exists'})
        if password == confirm_password:
            
            Usermodel(username=username, email=email, password=password).save()
            return redirect("/login")
        else:
            return render(request , "signup.html",{'message': 'password is incorrect'})
    return render(request, "signup.html")




def view_cart(request):
    
    user = Usermodel.objects.get(username='admin')
    cart_items = Cart.objects.filter(ordername=user)

    total_price = sum(item.order.orderitem.product_price for item in cart_items)
    tax = total_price * 0.1  # Assuming a 10% tax rate
    total = total_price + tax

    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'tax': tax,
        'total': total,
    }
    return render(request, 'cart.html', context)


def remove_from_cart(request, cart_id):
    print(cart_id,'------------------------------')
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('cart')