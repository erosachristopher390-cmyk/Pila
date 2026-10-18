
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        raise ValueError("La pila esta vacia.")

    def esta_vacia(self):
        return len(self.elementos) == 0


def operar(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
    elif operador == "^":
        return a ** b
    else:
        raise ValueError(f"Operador no valido: {operador}")


def evaluar(expresion, notacion):
    elementos = expresion.split()
    pila = Pila()
    operadores = {"+", "-", "*", "/", "^"}

    # En prefija se recorre de derecha a izquierda.
    if notacion == "prefija":
        elementos = elementos[::-1]

    for elemento in elementos:
        if elemento not in operadores:
            try:
                pila.apilar(float(elemento))
            except ValueError:
                raise ValueError(f"Elemento no valido: {elemento}")
        else:
            if len(pila.elementos) < 2:
                raise ValueError("La expresion esta incompleta.")

            if notacion == "posfija":
                b = pila.desapilar()
                a = pila.desapilar()
            else:
                a = pila.desapilar()
                b = pila.desapilar()

            pila.apilar(operar(a, b, elemento))

    if len(pila.elementos) != 1:
        raise ValueError("La expresion no es valida.")

    return pila.desapilar()


def main():
    print("=== EVALUADOR DE EXPRESIONES ===")
    print("1. Notacion posfija")
    print("2. Notacion prefija")

    opcion = input("Selecciona una opcion: ").strip()

    if opcion == "1":
        notacion = "posfija"
        print("Ejemplo: 5 3 + 2 *")
    elif opcion == "2":
        notacion = "prefija"
        print("Ejemplo: * + 5 3 2")
    else:
        print("Opcion no valida.")
        return

    expresion = input("Ingresa la expresion: ")

    try:
        resultado = evaluar(expresion, notacion)
        print("Resultado:", resultado)
    except (ValueError, OverflowError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
