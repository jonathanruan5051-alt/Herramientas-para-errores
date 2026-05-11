import logging

logging.basicConfig(filename='errores.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Función personalizada
class EdadInvalidaError(Exception):
    pass

try:
    # Validación de datos
    edad = int(input("Ingresa tu edad: "))

    # Assertion
    assert edad >= 0

    # Error personalizado
    if edad < 18:
        raise EdadInvalidaError("La persona es menor de edad.")

    # Operación normal
    print("Edad válida:", edad)

except ValueError:
    print("Error: Debes ingresar un número entero.")
    logging.error("El usuario ingresó un valor no numérico.")

except AssertionError:
    print("Error: La edad no puede ser negativa.")
    logging.error("El usuario ingresó una edad negativa.")

except EdadInvalidaError as e:
    print("Error personalizado:", e)
    logging.error(str(e))

finally:
    print("Programa finalizado.")