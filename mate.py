import cv2

conjuntoA = {2,4,5}
conjuntoB={5,2,3}
union = conjuntoA | conjuntoB
interseccion = conjuntoA & conjuntoB
diferencia = conjuntoA - conjuntoB
print("union",union)
print(f"interseccion {interseccion}")
print(f"diferencia {diferencia}")