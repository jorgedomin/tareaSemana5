# Programa para calcular el área de un rectángulo

# Función para calcular el área del rectángulo
def calcular_area_de_un_cuadrado(largo,ancho):
    """
    Esta función toma lado por lado y muestra el área.

    Parámetros:
    - largo (float): el largo del cuadrado.
    - ancho (float): ancho del cuadrado

    Retorna:
    float: El área del cuadrado.
    """
    area = largo * ancho
    return area


# Entrada de datos desde el usuario
largo_cuadrado = float(input("Ingrese  el largo del cuadrado: "))
ancho_cuadrado= float(input("Ingrese el ancho del cuadrado: "))

# Llamada a la función para calcular el área
area_resultante = calcular_area_de_un_cuadrado(largo_cuadrado, ancho_cuadrado)

# Mostrar el resultado
print(f"El largo {largo_cuadrado} y ancho {ancho_cuadrado} y su area resultante es: {area_resultante}")
