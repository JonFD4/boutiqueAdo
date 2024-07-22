from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """
    A view to return index page
    """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    product = Product.objects.get(pk=item_id)
    # Retrieve the quantity from the POST data and convert it to an integer
    quantity = int(request.POST.get('quantity', 0))
    size = None
    # Retrieve the redirect URL from the POST data
    redirect_url = request.POST.get('redirect_url')
    
    # Check if the product size is included in the POST 
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    
    # Retrieve the current shopping bag from the session, or initialize as an empty dictionary if not present
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Update size {size.upper()}{product.name} quantity to {bag[item_id]["item_by_size"][size]} ')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()}{product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()}{product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to your {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')
            
    # Update the session with the modified bag
    request.session['bag'] = bag
    
    # Redirect the user to the specified URL
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    # Adjust the quantity from the POST data and convert it to an integer
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 0))
    size = None

    # Check if the product size is included in the POST 
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    
    # Retrieve the current shopping bag from the session, or initialize as an empty dictionary if not present
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    # Update the session with the modified bag
    request.session['bag'] = bag
    
    # Redirect the user to the specified URL
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    try:
        product = get_object_or_404(Product, pk=item_id)
        # Remove the quantity from the POST data and convert it to an integer
        size = None
        # Check if the product size is included in the POST 
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})
        
        # Retrieve the current shopping bag from the session, or initialize as an empty dictionary if not present
        bag = request.session.get('bag', {})
        
        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
       
        # Update the session with the modified bag
        request.session['bag'] = bag
        
        # Redirect the user to the specified URL
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
