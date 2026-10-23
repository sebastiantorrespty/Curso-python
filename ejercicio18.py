precio = float(input("Ingrese el precio del producto: "))
if precio >= 100: 
    descuento = precio * 0.10
    precio_final = precio - descuento

    print("Precio final con descuento:" , precio_final)
else:
    precio_final = precio

    print("Precio final:" , precio_final)