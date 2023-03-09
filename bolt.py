# Datos del U-bolt
ancho = 0.5 # Ancho del U-bolt en pulgadas
altura = 1.0 # Altura del U-bolt en pulgadas
longitud = 3.0 # Longitud del U-bolt en pulgadas
esfuerzo_max = 80000.0 # Esfuerzo máximo de tensión en psi del acero utilizado

# Cálculo de la sección transversal y el área
area = ancho * altura # Área transversal en pulgadas cuadradas
perimetro = 2 * ancho + 2 * altura # Perímetro en pulgadas
diametro_promedio = perimetro / 3.1416 # Diámetro promedio en pulgadas
area_de_corte = 3.1416 / 4 * diametro_promedio ** 2 # Área de corte en pulgadas cuadradas

# Cálculo de la fuerza máxima que el U-bolt puede resistir antes de la falla
fuerza_maxima = esfuerzo_max * area_de_corte

# Imprimir los resultados
print("Área transversal del U-bolt: %.2f pulgadas cuadradas" % area)
print("Área de corte del U-bolt: %.2f pulgadas cuadradas" % area_de_corte)
print("Fuerza máxima que el U-bolt puede resistir antes de la falla: %.2f libras" % fuerza_maxima)

####
### Función para convertir libras a kilogramos
#def libras_a_kilos(peso_en_libras):
#    peso_en_kilos = peso_en_libras / 2.20462
#    return peso_en_kilos

# Ejemplo de uso de la función
#peso_en_libras = 100.0
#peso_en_kilos = libras_a_kilos(peso_en_libras)
#print("%.2f libras son %.2f kilos" % (peso_en_libras, peso_en_kilos))
########