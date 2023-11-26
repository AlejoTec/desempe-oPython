# Función para calcular la contaminación promedio en una lista de registros.
def calculate_average(records):
    total_pollution = sum(record[1] for record in records)
    average = total_pollution / len(records)
    return average

# Función para encontrar la ciudad con el máximo nivel de contaminación.
def city_with_max_pollution(data):
    city_max_pollution = max(data, key=lambda x: x[1])
    return city_max_pollution[0]

# Función para agregar un nuevo registro de contaminación a los datos existentes.
def add_record(data, city, pollution_level):
    new_record = (city, pollution_level)
    data.append(new_record)

# Función para mostrar datos de contaminación de todas las ciudades.
def display_data(data):
    for record in data:
        print(f"City: {record[0]}, Pollution Level: {record[1]}")

# Diccionario para almacenar datos de contaminación
pollution_data = []

# Agregar registros iniciales
add_record(pollution_data, "City A", 50)
add_record(pollution_data, "City B", 70)
add_record(pollution_data, "City C", 60)

# Mostrar datos iniciales
print("Initial data:")
display_data(pollution_data)

# Calcular y mostrar la contaminación promedio.
average = calculate_average(pollution_data)
print(f"Average pollution: {average}")

# Encuentra la ciudad con el nivel máximo de contaminación
max_city = city_with_max_pollution(pollution_data)
print(f"City with the maximum pollution level: {max_city}")

# Agregar un nuevo registro de contaminación
add_record(pollution_data, "City D", 90)

# Mostrar datos actualizadoss
print("\nUpdated data:")
display_data(pollution_data)
