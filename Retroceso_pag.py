
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        return self.elementos.copy()


class Navegador:
    def __init__(self):
        self.atras = Pila()
        self.adelante = Pila()
        self.actual = None

    def visitar(self, sitio):
        if self.actual is not None:
            self.atras.apilar(self.actual)

        self.actual = sitio
        self.adelante = Pila()

        print("Visitando:", self.actual)

    def regresar(self):
        if self.atras.esta_vacia():
            print("No hay paginas anteriores.")
            return

        self.adelante.apilar(self.actual)
        self.actual = self.atras.desapilar()
        print("Regresaste a:", self.actual)

    def avanzar(self):
        if self.adelante.esta_vacia():
            print("No hay paginas siguientes.")
            return

        self.atras.apilar(self.actual)
        self.actual = self.adelante.desapilar()
        print("Avanzaste a:", self.actual)

    def mostrar_historial(self):
        print("\n=== HISTORIAL DEL NAVEGADOR ===")

        if self.actual is None:
            print("No has visitado ningun sitio.")
            return

        print("Paginas anteriores:")
        anteriores = self.atras.mostrar()

        if anteriores:
            for sitio in reversed(anteriores):
                print("-", sitio)
        else:
            print("- Ninguna")

        print("Pagina actual:", self.actual)

        print("Paginas siguientes:")
        siguientes = self.adelante.mostrar()

        if siguientes:
            for sitio in reversed(siguientes):
                print("-", sitio)
        else:
            print("- Ninguna")


def main():
    navegador = Navegador()

    while True:
        print("\n=== MENU DEL NAVEGADOR ===")
        print("1. Visitar sitio web")
        print("2. Regresar")
        print("3. Avanzar")
        print("4. Mostrar historial")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            sitio = input("Escribe la URL del sitio: ").strip()

            if sitio:
                navegador.visitar(sitio)
            else:
                print("La URL no puede estar vacia.")

        elif opcion == "2":
            navegador.regresar()

        elif opcion == "3":
            navegador.avanzar()

        elif opcion == "4":
            navegador.mostrar_historial()

        elif opcion == "5":
            print("Cerrando el navegador.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
