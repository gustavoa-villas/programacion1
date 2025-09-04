def juego_vocales_consonantes():
    # Definimos las vocales
    vocales = "aeiou"

    # Ingreso de palabra
    palabra = input("Ingrese una palabra: ").lower()

    # Puntuaciones
    puntos_A = 0  # Jugador A (vocales)
    puntos_B = 0  # Jugador B (consonantes)

    # Recorremos cada posición de la palabra
    for i in range(len(palabra)):
        # Si es vocal, puntos para A
        if palabra[i] in vocales:
            puntos_A += len(palabra) - i
        else:  # Si es consonante, puntos para B
            puntos_B += len(palabra) - i

    # Mostramos resultados
    print(f"Jugador A (vocales): {puntos_A} puntos")
    print(f"Jugador B (consonantes): {puntos_B} puntos")

    # Determinamos ganador
    if puntos_A > puntos_B:
        print("Gana Jugador A (vocales)!")
    elif puntos_B > puntos_A:
        print("Gana Jugador B (consonantes)!")
    else:
        print("Empate!")


juego_vocales_consonantes()