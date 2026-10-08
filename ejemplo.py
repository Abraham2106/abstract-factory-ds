"""Abstract Factory: familias compatibles de botones y ventanas."""

from abc import ABC, abstractmethod


class FabricaInterfaz(ABC):
    """Declara las operaciones para crear productos relacionados."""

    @abstractmethod
    def crear_boton(self):
        pass

    @abstractmethod
    def crear_ventana(self):
        pass


class FabricaClara(FabricaInterfaz):
    """Crea únicamente componentes del tema claro."""

    def crear_boton(self):
        return BotonClaro()

    def crear_ventana(self):
        return VentanaClara()


class FabricaOscura(FabricaInterfaz):
    """Crea únicamente componentes del tema oscuro."""

    def crear_boton(self):
        return BotonOscuro()

    def crear_ventana(self):
        return VentanaOscura()


class Boton(ABC):
    """Interfaz abstracta del primer tipo de producto."""

    @abstractmethod
    def dibujar(self):
        pass


class BotonClaro(Boton):
    """Botón de la familia clara."""

    def dibujar(self):
        return "Botón claro: fondo blanco y texto negro"


class BotonOscuro(Boton):
    """Botón de la familia oscura."""

    def dibujar(self):
        return "Botón oscuro: fondo negro y texto blanco"


class Ventana(ABC):
    """Interfaz abstracta del segundo tipo de producto."""

    @abstractmethod
    def dibujar(self):
        pass


class VentanaClara(Ventana):
    """Ventana de la familia clara."""

    def dibujar(self):
        return "Ventana clara: panel blanco y borde gris"


class VentanaOscura(Ventana):
    """Ventana de la familia oscura."""

    def dibujar(self):
        return "Ventana oscura: panel negro y borde azul"


def construir_interfaz(fabrica):
    """Cliente: usa interfaces abstractas, sin conocer clases concretas."""
    boton = fabrica.crear_boton()
    ventana = fabrica.crear_ventana()
    return boton.dibujar(), ventana.dibujar()


def main():
    for fabrica in (FabricaClara(), FabricaOscura()):
        print(f"\nTema: {fabrica.__class__.__name__}")
        for componente in construir_interfaz(fabrica):
            print(" -", componente)


if __name__ == "__main__":
    main()
