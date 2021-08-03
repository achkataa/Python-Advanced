def stock_availability(products, action, *args):
    if action == "delivery":
        for product in args:
            products.append(product)
        return products
    else:
        if not args:
            products.pop(0)
            return products
        elif str(args[0]).isdigit():
            for i in range(args[0]):
                products.pop(0)
            return products
        else:
            unwanted = [product for product in products if product in args]
            return [item for item in products if item not in unwanted]





print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


