def leer_float(mensaje, minimo=None):
    while True:
        entrada = input(mensaje).replace(",", ".")
        try:
            valor = float(entrada)
            if minimo is not None and valor < minimo:
                print(f"Por favor, ingresá un valor mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingresá un número.")

def main():
    print("=== Calculadora de costos de producción ===")
    costo_leche = leer_float("Costo total de la leche: $", 0)
    costo_fermento = leer_float("Costo del fermento o insumos base: $", 0)
    costo_envases = leer_float("Costo total de los envases: $", 0)

    unidades = leer_float("¿Cuántas unidades se produjeron en total?: ", 1)
    unidades = int(unidades)

    costo_total = costo_leche + costo_fermento + costo_envases
    costo_por_unidad = costo_total / unidades

    print("\n--- Resumen de costos ---")
    print(f"Costo total de producción: ${costo_total:.2f}")
    print(f"Costo de producción por unidad: ${costo_por_unidad:.2f}")

    porcentaje_ganancia = leer_float("¿Qué porcentaje de ganancia deseás? (%): ", 0)
    precio_venta = costo_por_unidad * (1 + porcentaje_ganancia / 100)

    print("\n--- Precio sugerido ---")
    print(f"Precio final de venta sugerido por unidad: ${precio_venta:.2f}")

if __name__ == "__main__":
    main()