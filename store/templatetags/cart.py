from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product_id, cart):
    # print(product_id)
    keys=cart.keys()
    # print(keys)
    for i in keys:
        # print(type(i),type(product_id.id))
        if int(i)==product_id.id:
            return True
    return False    


@register.filter(name='cart_quantity')
def cart_quantity(product_id, cart):
    keys=cart.keys()
    for i in keys:
        if int(i)==product_id.id:
            return cart.get(i)
    return 0   


@register.filter(name='total_price')
def total_price(product, cart):
    return product.price * cart_quantity(product, cart)  

@register.filter(name='total_cart_price')
def total_cart_price(product, cart):
    s=0
    for p in product:
        s+= total_price(p, cart)
    return s  

@register.filter(name='multiply')
def multiply(num1,num2):
    return num1*num2