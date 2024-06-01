import math
def redondear(numero):
    if numero > 3.50:
        return math.ceil(numero)
    else:
        return math.floor(numero)

