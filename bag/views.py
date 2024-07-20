from django.shortcuts import render ,redirect

def view_bag(request):
    """
    A view to return index page
    """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    # Retrieve the quantity from the POST data and convert it to an integer
    quantity = int(request.POST.get('quantity'))
    # Retrieve the redirect URL from the POST data
    redirect_url = request.POST.get('redirect_url')
    # Retrieve the current shopping bag from the session, or initialize as an empty dictionary if not present
    bag = request.session.get('bag', {})

    # Check if the item is already in the bag
    if item_id in list(bag.keys()):
        # If it is, increase the quantity by the specified amount
        bag[item_id] += quantity
    else:
        # If not, add the item to the bag with the specified quantity
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
