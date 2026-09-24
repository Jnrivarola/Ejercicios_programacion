"""Ejercicio N°3

Calculadora de descuento

Ahora debes generar un programa calcule el descuento de un producto, se le solicita
al usuario ingresar el precio original de un producto. Luego, calcula y muestra el precio final 
después del descuento. 
Tener en cuenta lo siguiente: 
Si se ingresa un precio de producto mayor o igual a $12.999 entonces se realizará 
el descuento del 30%, 
Sino, se realizará el descuento del 20% sobre el total del producto."""

precio = float(input("Ingrese el precio original del producto: $"))
if precio >= 12999:
    descuento = precio * 0.30
    
else:
    descuento = precio * 0.20
    
precio_final = precio - descuento
print(f"Descuento aplicado: ${descuento:.2f}.")
print(f"Precio final con descuento: ${precio_final:.2f}")
