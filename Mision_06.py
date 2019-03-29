#Roberto Castro Barrios A01748559
# Descripción: Programa que te permite hacer diferentes figuras.

import pygame   # Librería de pygame
import math as m # Librería de math
import random as r

# Dimensiones de la pantalla
ANCHO = 600
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


def generarColorAleatorio ():
    rojo = r.randint(0, 255)
    verde = r.randint(0, 255)
    azul = r.randint(0, 255)
    return (rojo, verde, azul)



# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        k = r/R
        P = r//m.gcd(r, R)

        for angulo in range(0, (360 + 1)*P*2, 1):
            cAleatorio = generarColorAleatorio()
            a = m.radians(angulo)
            x = int(R * (((1-k) * m.cos(a)) + ((l * k) * m.cos(((l-k) / k) * a))))
            y = int(R * (((1-k) * m.sin(a)) - ((l * k) * m.sin(((l-k) / k) * a))))
            pygame.draw.circle(ventana, cAleatorio, (x + ANCHO // 2, ALTO // 2 - y), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(60)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = int(input("Ingresa el valor de r: "))
    R = int(input("Ingresa el valor de R: "))
    l = float(input("Ingresa el valor de l: "))
    dibujar(r, R, l)



# Llamas a la función principal
main()