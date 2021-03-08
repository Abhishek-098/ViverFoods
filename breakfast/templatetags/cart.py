from django import template

register = template.Library()


@register.filter(name = 'is_incart')
def is_incart(pid,cart):
    keys = cart.keys()
    #print(cart)
    #print(keys)
    for id in keys:
        #print(id , pid.id)
        #print(type(id),type(pid.id))
        if int(id) == pid.id:
            return True
    return False  

@register.filter(name = 'cart_qty')
def cart_qty(pid,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == pid.id:
            return cart.get(id)
    return 0



@register.filter(name = 'price_total')
def price_total(pid,cart):
    return pid.price*cart_qty(pid,cart)



@register.filter(name = 'total_cart_price')
def total_cart_price(products,cart):
    sum=0
    count = 0
    for p in products:
        sum += price_total(p,cart)
        count+=1
    
      
    return sum

@register.filter(name = 'total_cart_items')
def total_cart_items(products,cart):
    
    count = 0
    for p in products:
        
        count+=1
    #print(count)
      
    return count

