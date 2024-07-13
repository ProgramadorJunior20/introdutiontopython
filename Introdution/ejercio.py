#Ejercicio 2

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, 
#así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
#Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, 
#realiza un programa que muestre el peso total de toda la venta.

#Pista: Suponiendo que un cliente pide 5 payasos y 3 muñecas, 
#la juguetería debería hacer la multiplicación de la cantidad de payasos con su peso, 
#al igual que las muñecas; al tener ambos totales de peso, se debe sumar.
#estas constantes no cambian de valor

PESO_PAYASO = 112;
PESO_MUNNECA = 75;

#catidad de pruducto pedido
cantidad_payaso = 23;
cantidad_munneca = 54;

#multiplicamos caltidad de payasos y muñecas pedidos por el peso de cada uno
peso_total_payaso = cantidad_payaso * PESO_PAYASO;
peso_total_munneca = cantidad_munneca * PESO_MUNNECA;

#sumamos peso total de payasos y muñacas para octener el peso de la venta
peso_total_venta = peso_total_payaso + peso_total_munneca;


print(f"Peso total de payasos: {peso_total_payaso} g")
print(f"Peso total de muñecas: {peso_total_munneca} g")
print(f"Peso total de la venta: {peso_total_venta} g")
