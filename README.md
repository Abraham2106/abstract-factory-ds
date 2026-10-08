# Abstract Factory: interfaz clara y oscura

## Que corre

Implementacion de Abstract Factory en Python. Se utilizan fabricas para crear objetos de una misma familia, como botones y ventanas de tema claro u oscuro, haciendo que sus componentes sean compatibles.

## Como se corre

```bash
python demo.py
```

Se vera la siguiente salida:

```text
Tema: FabricaClara
 - Boton claro: fondo blanco y texto negro
 - Ventana clara: panel blanco y borde gris

Tema: FabricaOscura
 - Boton oscuro: fondo negro y texto blanco
 - Ventana oscura: panel negro y borde azul
```

Para ejecutar las pruebas:

```bash
python -m pip install pytest
python -m pytest -q
```
