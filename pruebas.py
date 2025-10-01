import math
f1 = f2 = f3 = 5
porcentaje = 0.55

ventas = f1 + f2 + f3
pagado = ventas * porcentaje
decimal = pagado - int(pagado)
if decimal <= 0.5:
     pagado = math.floor(pagado)
else:
     pagado = math.ceil(pagado)
print(pagado)