 # Lista de productos, cada producto es una tupla (nombre, precio, cantidad en stock)
products = [
    ("T-shirt", 20.0, 50),
    ("Pants", 40.0, 30),
    ("Shoes", 60.0, 20),
    ("Hat", 15.0, 10)
]

# Función lambda para calcular el valor total de un producto en stock (precio * cantidad)
calculate_total_value = lambda product: product[1] * product[2]

## Función lambda para filtrar productos con un precio mayor que cierto umbral
filter_expensive_products = lambda product, threshold: product[1] > threshold

# Función lambda para ordenar la lista de productos por precio
sort_by_price = lambda product: product[1]

# Calcular el valor total de cada producto en stock
total_values = list(map(calculate_total_value, products))

# Filtrar productos con un precio mayor a $30
expensive_products = list(filter(lambda x: filter_expensive_products(x, 30), products))

# Ordenar la lista de productos por precio de forma ascendente
products.sort(key=sort_by_price)

# Mostrar los resultados
print("Total value of each product in stock:")
for product, total_value in zip(products, total_values):
    print(f"{product[0]} - Total Value: ${total_value}")

print("\nProducts with a price greater than $30:")
for product in expensive_products:
    print(f"{product[0]} - Price: ${product[1]}")

print("\nProducts sorted by price in ascending order:")
for product in products:
    print(f"{product[0]} - Price: ${product[1]}")