from django import template

register=template.Library()

@register.filter(name='symble')
def symble(total_price):
    return '₹'+str(total_price)