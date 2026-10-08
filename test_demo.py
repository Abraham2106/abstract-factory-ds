"""Pruebas que verifican las ideas principales de Abstract Factory."""

import pytest

from demo import (
    Boton,
    BotonClaro,
    BotonOscuro,
    FabricaClara,
    FabricaInterfaz,
    FabricaOscura,
    Ventana,
    VentanaClara,
    VentanaOscura,
    construir_interfaz,
)


@pytest.mark.parametrize(
    "fabrica,clase_boton,clase_ventana",
    [
        (FabricaClara(), BotonClaro, VentanaClara),
        (FabricaOscura(), BotonOscuro, VentanaOscura),
    ],
)
def test_cada_fabrica_crea_una_familia_compatible(
    fabrica, clase_boton, clase_ventana
):
    """Comprueba que cada fabrica produzca componentes compatibles."""
    boton = fabrica.crear_boton()
    ventana = fabrica.crear_ventana()

    assert isinstance(boton, clase_boton)
    assert isinstance(ventana, clase_ventana)
    assert isinstance(boton, Boton)
    assert isinstance(ventana, Ventana)


def test_nueva_familia_funciona_sin_cambiar_el_cliente():
    """Comprueba que el cliente admita una nueva familia sin cambios."""

    class BotonAltoContraste(Boton):
        def dibujar(self):
            return "Boton de alto contraste"

    class VentanaAltoContraste(Ventana):
        def dibujar(self):
            return "Ventana de alto contraste"

    class FabricaAltoContraste(FabricaInterfaz):
        def crear_boton(self):
            return BotonAltoContraste()

        def crear_ventana(self):
            return VentanaAltoContraste()

    assert construir_interfaz(FabricaAltoContraste()) == (
        "Boton de alto contraste",
        "Ventana de alto contraste",
    )

    resultado_claro = construir_interfaz(FabricaClara())
    resultado_nuevo = construir_interfaz(FabricaAltoContraste())

    assert resultado_claro != resultado_nuevo
