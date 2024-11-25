from django.shortcuts import render, redirect, get_object_or_404
from store.models import Medicine
from .models import Cart, CartItem
from django.contrib import messages

# Add item to cart
def add_to_cart(request, medicine_id, quantity=1):
    # Get or create the cart for the current user
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    # Get the medicine object
    medicine = get_object_or_404(Medicine, id=medicine_id)

    # Get or create a cart item for the medicine
    cart_item, created = CartItem.objects.get_or_create(cart=cart, medicine=medicine)

    # If the item already exists, update the quantity
    cart_item.quantity += quantity
    cart_item.save()

    return redirect('view_cart')  # Redirect to the view cart page


def minus_to_cart(request, medicine_id, quantity=1):
    # Get or create the cart for the current user
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    # Get the medicine object
    medicine = get_object_or_404(Medicine, id=medicine_id)

    # Get the cart item for the medicine
    cart_item = get_object_or_404(CartItem, cart=cart, medicine=medicine)

    # Check if the quantity can be reduced
    if cart_item.quantity < quantity:
        if quantity == 1:
            messages.warning(request, "Cannot reduce quantity below 1.")
        elif quantity == 10:
            messages.warning(request, "Cannot reduce quantity below 10.")
    else:
        cart_item.quantity -= quantity
        if cart_item.quantity == 0:
            cart_item.delete()  # Remove the item from the cart if quantity becomes 0
        else:
            cart_item.save()
    
    return redirect('view_cart')  # Redirect to the view cart page

# View cart
def view_cart(request):
    # Get the cart for the current user
    cart = get_object_or_404(Cart, user=request.user)
    
    # Render the cart page with the cart object
    return render(request, 'cart.html', {'cart': cart})

# Remove item from cart
def remove_from_cart(request, item_id):
    # Get the cart item and ensure it belongs to the current user's cart
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    # Delete the cart item
    cart_item.delete()

    return redirect('view_cart')  # Redirect to the view cart page

def checkout(request):
    return render(request, 'checkout.html')