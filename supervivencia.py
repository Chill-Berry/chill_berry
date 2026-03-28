import random

def main():
    # Valores iniciales
    salud = 100
    comida = 50
    agua = 50
    dia = 1

    print("Bienvenido al juego de supervivencia en la naturaleza.")
    print("Tu objetivo es sobrevivir el mayor tiempo posible.")
    print("Empiezas con 100 de salud, 50 de comida y 50 de agua.")

    while salud > 0 and comida > 0 and agua > 0:
        print(f"\n--- Día {dia} ---")
        print(f"Salud: {salud}, Comida: {comida}, Agua: {agua}")
        print("¿Qué querés hacer?")
        print("1. Buscar comida")
        print("2. Buscar agua")
        print("3. Descansar (recupera salud)")

        accion = input("Elige una acción (1/2/3): ").strip()
        print()
        if accion == "1":
            # Buscar comida: hay una probabilidad de éxito
            exito = random.random()
            if exito < 0.7:
                encontrado = random.randint(10, 25)
                comida += encontrado
                print(f"¡Has encontrado {encontrado} puntos de comida!")
            else:
                print("No encontraste nada para comer hoy.")
                salud -= 5  # Buscar sin éxito puede agotar
                print("Te agotas buscando en vano (-5 salud)")
        elif accion == "2":
            # Buscar agua: probabilidad de éxito
            exito = random.random()
            if exito < 0.7:
                encontrado = random.randint(10, 25)
                agua += encontrado
                print(f"¡Has encontrado {encontrado} puntos de agua!")
            else:
                print("No encontraste agua potable hoy.")
                salud -= 5  # Buscar sin éxito puede agotar
                print("Sufres deshidratación buscando en vano (-5 salud)")
        elif accion == "3":
            # Descansar: recupera salud, pero no se obtiene comida ni agua
            ganancia = random.randint(10, 20)
            salud = min(100, salud + ganancia)
            print(f"Descansas bien y recuperas {ganancia} de salud (máx 100).")
        else:
            print("Acción no válida. Pierdes el día de confusión.")
            salud -= 3

        # Gasto vital por pasar el día
        comida -= 7  # Se consume 7 de comida por día
        agua -= 7    # Se consume 7 de agua por día

        # Eventos aleatorios al final del día
        evento = random.random()
        if evento < 0.15:
            # Encuentra refugio: bonificación
            print("¡Has encontrado un refugio seguro (+10 salud)!")
            salud = min(100, salud + 10)
        elif evento < 0.30:
            # Ataque animal: pierde salud
            dano = random.randint(10, 25)
            print(f"¡Un animal salvaje te ataca! Pierdes {dano} de salud.")
            salud -= dano
        elif evento < 0.40:
            # Comida se echa a perder
            perdida = random.randint(5, 15)
            comida = max(0, comida - perdida)
            print(f"Parte de tu comida se ha echado a perder (-{perdida} comida).")
        elif evento < 0.50:
            # Pierde algo de agua
            perdida = random.randint(5, 15)
            agua = max(0, agua - perdida)
            print(f"Parte de tu agua se ha derramado o evaporado (-{perdida} agua).")
        # Otros eventos pueden agregarse...

        # Comprobar si algún recurso crítico llegó a cero
        if salud <= 0:
            print("\nTu salud ha llegado a 0. Has muerto.")
            break
        if comida <= 0:
            print("\nTe has quedado sin comida. Has muerto de inanición.")
            break
        if agua <= 0:
            print("\nTe has quedado sin agua. Has muerto de deshidratación.")
            break

        dia += 1

    print(f"\n--- Game Over ---")
    print(f"Sobreviviste {dia} día(s). ¡Gracias por jugar!")

if __name__ == "__main__":
    main()