import random
import string

# Definimos una función para generar una contraseña segura
def generar_contraseña(longitud=12):
    # Definimos los posibles caracteres: mayúsculas, minúsculas, dígitos y símbolos
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    digitos = string.digits
    simbolos = string.punctuation

    # Nos aseguramos de incluir al menos un carácter de cada tipo
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(digitos),
        random.choice(simbolos)
    ]

    # Llenamos el resto de la contraseña con una mezcla aleatoria de todos los caracteres
    todos = mayusculas + minusculas + digitos + simbolos
    for _ in range(longitud - 4):
        contraseña.append(random.choice(todos))

    # Mezclamos la lista para que la ubicación de los caracteres obligatorios sea aleatoria
    random.shuffle(contraseña)

    # Unimos la lista para formar la cadena final
    return ''.join(contraseña)

# Pedimos al usuario la longitud de la contraseña y validamos la entrada
if __name__ == "__main__":
    entrada = input("¿De cuántos caracteres querés la contraseña? (mínimo 4): ")
    try:
        longitud = int(entrada)
        if longitud < 4:
            print("Por favor, ingresá un número mayor o igual a 4.")
        else:
            print("Contraseña segura generada:", generar_contraseña(longitud))
    except ValueError:
        print("Por favor, ingresá un número válido.")