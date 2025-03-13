import json

# 1️⃣ Leer el archivo datos.json
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)  # Cargar datos del JSON

# 2️⃣ Mostrar información de la tienda
print(f"📢 Tienda: {datos['tienda']}")
print("📦 Productos disponibles:")

# 3️⃣ Recorrer los productos y mostrarlos
for producto in datos["productos"]:
    print(f"  - {producto['nombre']} (${producto['precio']}) - Stock: {producto['stock']}")

# 4️⃣ Buscar productos con bajo stock (< 5)
productos_bajo_stock = [p for p in datos["productos"] if p["stock"] < 5]

if productos_bajo_stock:
    print("\n⚠️ Productos con bajo stock:")
    for p in productos_bajo_stock:
        print(f"  - {p['nombre']} ({p['stock']} unidades)")
else:
    print("\n✅ No hay productos con bajo stock")

# 5️⃣ Calcular el total del inventario en dinero
total_inventario = sum(p["precio"] * p["stock"] for p in datos["productos"])
print(f"\n💰 Valor total del inventario: ${total_inventario:.2f}")
