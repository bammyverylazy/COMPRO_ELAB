products = {
    "apple": {"price": 20, "stock": 10},
    "banana": {"price": 15, "stock": 5},
    "orange": {"price": 30, "stock": 3}
}

orders = [
    "apple,3",
    "banana,2",
    "orange,5",
    "grape,1",
    "apple,0",
    "banana,abc"
]

class ProductNotFoundError(Exception):
    pass
class InvalidQuantityError(Exception):
    pass
class OutOfStockError(Exception):
    pass

print("Processing orders...")
print()
price = 0
for order in orders:
    try:
        print(f"Order: {order}")
        product, quantity = order.split(",")
        quantity = int(quantity)
        if quantity <0:
            raise InvalidQuantityError("Quantity must be a positive integer.")
        if product not in products:
            raise ProductNotFoundError(f"Product '{product}' was not found.")
        if products[product]["stock"] < quantity:
            raise OutOfStockError(f"Not enough stock for {product}.")
        price += products[product]["price"]*int(quantity)
    except ValueError:
        print(f"ERROR - Invalid quantity: {product}")
    except Exception as e:
        print(f"ERROR - {e}")
    else :
        print(f"SUCCESS - {quantity} {product}(s) purchased. Total: ${price}")
    finally:
        print("Order processing finished.")
        print()
print("Processing complete.")
print()
print("Final stock:")