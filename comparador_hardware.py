# Comparador de hardware y armador de presupuestos

# Diccionario de procesadores disponibles y sus precios en dólares
procesadores = [
    {"nombre": "AMD Ryzen 5 5600G", "precio": 120},
    {"nombre": "Intel Core i5 12400F", "precio": 180},
    {"nombre": "Intel Core i9 13900K", "precio": 580},
]

# Diccionario de tarjetas gráficas disponibles y sus precios en dólares
graficas = [
    {"nombre": "NVIDIA RTX 3060", "precio": 320},
    {"nombre": "AMD RX 6800 XT", "precio": 560},
    {"nombre": "AMD RX 7900 XTX", "precio": 950},
]

def mostrar_opciones(componentes):
    """Imprime la lista numerada de opciones de hardware."""
    for idx, comp in enumerate(componentes, 1):
        print(f"{idx}. {comp['nombre']} - ${comp['precio']}")

def leer_opcion(mensaje, opciones):
    """Lee una opción válida del usuario (número de lista)."""
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if 1 <= valor <= len(opciones):
                return valor - 1  # Índice en la lista
            else:
                print("Por favor, elegí una opción válida del listado.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresá un número.")

def main():
    print("=== Comparador y armador de presupuesto de hardware ===\n")

    print("Procesadores disponibles:")
    mostrar_opciones(procesadores)
    idx_proc = leer_opcion("Elegí el número de procesador: ", procesadores)
    proc_seleccionado = procesadores[idx_proc]

    print("\nTarjetas gráficas disponibles:")
    mostrar_opciones(graficas)
    idx_graf = leer_opcion("Elegí el número de gráfica: ", graficas)
    graf_seleccionada = graficas[idx_graf]

    print("\n--- Resumen de tu presupuesto ---")
    print(f"Procesador elegido: {proc_seleccionado['nombre']} (${proc_seleccionado['precio']})")
    print(f"Gráfica elegida:   {graf_seleccionada['nombre']} (${graf_seleccionada['precio']})")

    total = proc_seleccionado['precio'] + graf_seleccionada['precio']
    print(f"\nCosto total estimado: ${total}")

    # Lógica de cuello de botella simple: procesador más barato y gráfica más cara
    if idx_proc == 0 and idx_graf == len(graficas) - 1:
        print("\nADVERTENCIA: Posible Cuello de Botella ⚠️")
        print("El procesador más barato puede limitar el rendimiento de la gráfica seleccionada.")

if __name__ == "__main__":
    main()