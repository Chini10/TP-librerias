    #               TP 6 L&BRER&AS...
from paquete_redondear import redondear
import datetime,random,time

"""1. Escriba una función redondear() que permita redondear un número 
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el 
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente 
anterior (3).  """

#def redondear(numero):
#    if numero > 3.50:
#        return math.ceil(numero)
#    else:
#        return math.floor(numero)

numero = 3.6
num_redondeado = redondear(numero)
print(f"El número redondeado es:{num_redondeado}")

"""2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un 
módulo que esté fuera de ese paquete, cree una función de suma de 
decimales que redondee el resultado haciendo uso de la función 
redondear() del paquete recién creado. """

def suma_decimales(a, b):
    resultado = a + b
    return redondear(resultado)

inicio_suma_decimales = time.time()
num1 = 3.6
num2 = 2.4
result_suma = suma_decimales(num1, num2)
fin_suma_decimales = time.time()

print(f"La suma de {num1} y {num2} redondeada es: {result_suma}")
print("Tiempo de ejecución de la suma de decimales:", fin_suma_decimales - inicio_suma_decimales, "segundos")

"""3. Usando el módulo datetime, escribe un programa que muestre la fecha 
y hora actuales del sistema. """

"""4. Escriba un programa que devuelva un número par al azar entre 2 y 10 
(pista: para comprobar si se pueden generar todos los números, pruebe 
ejecutar el programa dentro de un ciclo infinito). """

"""5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado 
para la adivinación o para buscar consejo. Su mecanismo es muy simple: 
ante una pregunta del usuario, la bola responde con una de 8 posibles 
respuestas: - - - - - - - - 
Es seguro que sí 
Las chances son buenas 
Puedes contar con ello 
Pregúntame de nuevo más tarde 
Concéntrate y pregunta de nuevo 
No veo con claridad, intenta de nuevo 
Mi respuesta es no 
Mis fuentes me dicen que no 
Escriba una función en Python para simular la bola mágica. """

"""6. Encuentre el tiempo de ejecución de los programas de los ejercicios 
anteriores (pista: use el módulo time) """

def bola_magica():
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    return random.choice(respuestas)

def obtener_numero_par_aleatorio():
    numero = random.randint(1, 5) * 2
    return numero

def medir_tiempo_ejecucion(funcion):
    inicio = time.time()
    resultado = funcion()
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return resultado, tiempo_ejecucion

pregunta = input("Hazme una pregunta: ")
respuesta_bola_magica, tiempo_ejecucion_bola_magica = medir_tiempo_ejecucion(bola_magica)
print("Respuesta de la bola mágica:", respuesta_bola_magica)
print("Tiempo de ejecución de la bola mágica:", tiempo_ejecucion_bola_magica, "segundos")

numero_par_aleatorio, tiempo_ejecucion_numero_par = medir_tiempo_ejecucion(obtener_numero_par_aleatorio)
print("Número par aleatorio entre 2 y 10:", numero_par_aleatorio)
print("Tiempo de ejecución de obtener un número par aleatorio:", tiempo_ejecucion_numero_par, "segundos")

inicio = time.time()
fecha_hora_actual = datetime.datetime.now()
fin = time.time()
tiempo_ejecucion_fecha_hora_actual = fin - inicio
print("Fecha y hora actuales del sistema:", fecha_hora_actual)
print("Tiempo de ejecución de obtener la fecha y hora actuales:", tiempo_ejecucion_fecha_hora_actual, "segundos")




"""7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde 
toman uno o más papeles al azar de un pozo para elegir los ganadores. """

def sorteo(participantes, cantidad_ganadores):
    ganadores = random.sample(participantes, cantidad_ganadores)
    return ganadores

participantes = ["Amelina", "Cristian", "Jessica", "Emma", "Ana","Luz","Alguien","Val"]
cantidad_ganadores = 2
ganadores = sorteo(participantes, cantidad_ganadores)

print("Ganadores del sorteooooo...")
for i, ganador in enumerate(ganadores, start=1):
    print(f"Ganador {i}: {ganador}")
