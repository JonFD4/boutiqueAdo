from django.shortcuts import render ,redirect

def view_bag(request):
    """
    A view to return index page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
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
               
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            
    # Update the session with the modified bag
    request.session['bag'] = bag
    
    # Redirect the user to the specified URL
    return redirect(redirect_url)







#Notes
"""
Session Explanation:
Modern web applications often use sessions to store data that should persist 
across multiple requests from the same client. 
Sessions are typically maintained using cookies. 
The session data can include anything that needs to be remembered between requests,
like the contents of a shopping bag in an e-commerce application.

"""
