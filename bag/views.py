from django.shortcuts import render

def view_bag(request):
    """
    A view to return index page
    """
    return render(request, 'bag/bag.html')

