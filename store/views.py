from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.productorder import ProductOrder
from django.contrib import messages 
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    fd=Product.objects.all()
    fd2=Category.objects.all()
    paginator=Paginator(fd,4)
    page_no=request.GET.get("page")
    productData=paginator.get_page(page_no)
    total_page=productData.paginator.num_pages
    data={
        'productdata':productData,
        "product":fd2,
        "last_page":total_page,
        "totalpagelist":[n+1 for n in range(total_page)]

    }
    return render(request,"home.html",data)


    
def category(request, m_id):
    if m_id>0:
        mdata=Product.objects.filter(category=Category.objects.get(id=m_id))
        
    else: 
        mdata=Product.objects.all()
    fd2=Category.objects.all()
    paginator=Paginator(mdata,4)
    page_no=request.GET.get("page")
    productData=paginator.get_page(page_no)
    total_page=productData.paginator.num_pages
    error=""
    if len(mdata)==0:
        error="Please Add Product"
    data={
        
        "productdata":productData,
        "product":fd2,
        "error":error,
        "last_page":total_page,
        "totalpagelist":[n+1 for n in range(total_page)]
    }
  
    return render(request,"home.html",data)

def cart(request):
    try:
        if request.method=="POST":
            product_id=request.POST.get("product")
            remove=request.POST.get("remove")
            cart=request.session.get('cart')
            if cart:
                quantity=cart.get(product_id)
                if quantity:
                    if remove:
                        if quantity <=1:
                            cart.pop(product_id)
                           
                        else:    
                            cart[product_id]=quantity-1
                    else:  
                        cart[product_id]=quantity+1            
                else:
                    cart[product_id]=1
            else:
                cart={}
                cart[product_id]=1
                request.session['cart']=cart   
                return redirect("home")   
            request.session['cart']=cart   
              
            #   add product cart in session
       
    except:
        messages.success(request, 'failed')

    return redirect('home')
    
def showcart(request):
    product_key=request.session.get('cart')
    if product_key:
    
        product_key=list(request.session.get('cart').keys())
        product=Product.objects.filter(id__in=product_key)
    else:
        product=""
    # print(request.session.get("customer_id"))    
    return render(request,'showcart.html',{"product":product})

def checkout(request):
    try:
        if request.method=="POST":
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            customer_id=request.session.get("customer_id")
            cdata=request.session.get("cart")
            item=cdata.keys()
            product=Product.objects.filter(id__in=item)
     
            for i in product:
                order=ProductOrder(customer=Customer(id=customer_id),
                                   product=i,
                                   price=i.price,
                                   address=address,
                                   mobile=phone,
                                   quantity=cdata.get(str(i.id))
                                )
                order.save()                   
            request.session['cart']={}     
                                                            
    except:
        pass        
    return redirect("cart")

def orderdisplay(request):
    customer_id=request.session.get("customer_id")
    orders=ProductOrder.get_orders_by_customer(customer_id)
    return render(request,'order_display.html',{"orders":orders})

def usersignup(request):
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            password=request.POST.get('password')
            # passwod ko hash kr dega
            # password=make_password(password)
            em=Customer(name=name, mobile=mobile, email=email, password=password)
            em.save()
            messages.success(request, 'Registration Successful')
    except:
        messages.error(request, 'Registration Fail Please Enter Valid Data--')
    return redirect('home')        

def userlogin(request):
    try:
        if request.method=="POST":
            email=request.POST.get('email')
            password=request.POST.get('password')
            fdata=Customer.objects.all()
            for i in fdata:
                # print(i.id)
                if i.email==email and i.password==password:
                    request.session['email']=email
                    request.session['password']=password
                    request.session["username"]=i.name 
                    request.session["customer_id"]=i.id
                    messages.success(request, 'login successful--')

            return redirect('home') 

    except:
        messages.error(request, 'Invalid Email/Password')
    # print(request.session.get("customer_id"))
    return redirect('home')  
    
def userlogout(request):
    request.session.clear()
    # clear session
    messages.error(request, 'User Logout--')
    return redirect("home")