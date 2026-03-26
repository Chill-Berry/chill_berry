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

# Llamamos a la función y mostramos la contraseña generada
if __name__ == "__main__":
    print("Contraseña segura generada:", generar_contraseña())