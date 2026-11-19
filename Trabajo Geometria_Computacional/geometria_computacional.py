"""Herramientas para el taller de Geometría Computacional.

Coordenadas: tuplas (x, y). No requiere paquetes externos.
Ejercicios cubiertos: orientación, intersección de segmentos,
comparación de pares, conteo de triangulación y crecimiento asintótico.
"""


def orientacion(a, b, c):
    """Devuelve el determinante orientado de A, B y C.

    > 0: giro antihorario; < 0: giro horario; == 0: puntos colineales.
    Complejidad temporal: O(1).
    """
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def en_segmento(a, p, b):
    """Indica si P está dentro de la caja delimitadora del segmento AB."""
    return (min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


def intercepta(a, b, c, d):
    """Determina si los segmentos AB y CD se cruzan, tocan o se solapan.

    Complejidad temporal: O(1), pues se hacen cuatro orientaciones
    y un número fijo de comparaciones.
    """
    o1 = orientacion(a, b, c)
    o2 = orientacion(a, b, d)
    o3 = orientacion(c, d, a)
    o4 = orientacion(c, d, b)

    # Cruce propio: cada segmento deja los extremos del otro en lados opuestos.
    if (((o1 > 0 and o2 < 0) or (o1 < 0 and o2 > 0))
            and ((o3 > 0 and o4 < 0) or (o3 < 0 and o4 > 0))):
        return True

    # Contacto en extremos o solapamiento colineal.
    if o1 == 0 and en_segmento(a, c, b):
        return True
    if o2 == 0 and en_segmento(a, d, b):
        return True
    if o3 == 0 and en_segmento(c, a, d):
        return True
    if o4 == 0 and en_segmento(c, b, d):
        return True
    return False


def pares_intersectados(segmentos):
    """Devuelve los índices de todos los pares de segmentos que se intersecan.

    Cada par no ordenado se examina una sola vez. Complejidad: O(n^2).
    """
    encontrados = []
    n = len(segmentos)
    for i in range(n):
        for j in range(i + 1, n):
            if intercepta(*segmentos[i], *segmentos[j]):
                encontrados.append((i, j))
    return encontrados


def contar_pares(n):
    """Número de pares no ordenados: n(n-1)/2."""
    if n < 0:
        raise ValueError("n no puede ser negativo")
    return n * (n - 1) // 2


def triangulos_y_diagonales(n):
    """Para un polígono simple: devuelve (n-2 triángulos, n-3 diagonales)."""
    if n < 3:
        raise ValueError("Un polígono debe tener al menos 3 vértices")
    return n - 2, n - 3


def comparar_crecimiento(n, c_a=1, c_b=1):
    """Evalúa los modelos T_A(n)=c_A*n^2 y T_B(n)=c_B*n^3."""
    if n < 0:
        raise ValueError("n no puede ser negativo")
    return c_a * n**2, c_b * n**3


if __name__ == "__main__":
    print("EJERCICIO 1 — Orientación")
    casos_orientacion = [
        ((1, 2), (5, 3), (3, 7)),
        ((2, 1), (6, 5), (8, 2)),
        ((1, 1), (3, 3), (6, 6)),
        ((0, 4), (5, 4), (3, 1)),
    ]
    for puntos in casos_orientacion:
        d = orientacion(*puntos)
        sentido = "antihorario" if d > 0 else "horario" if d < 0 else "colineal"
        print(f"{puntos}: D={d} -> {sentido}")

    print("\nEJERCICIO 2 — Intersección de segmentos")
    casos_segmentos = [
        ((1, 1), (7, 5), (2, 6), (8, 1)),
        ((1, 1), (3, 3), (5, 5), (7, 7)),
        ((0, 2), (6, 2), (3, 2), (9, 2)),
    ]
    for i, caso in enumerate(casos_segmentos, start=1):
        print(f"Caso {i}: {intercepta(*caso)}")

    print("\nEJERCICIO 3 — Comparación de todos los pares")
    print("Pares para n=5:", contar_pares(5))
    print("Pares para n=8:", contar_pares(8))
    print("Pares para n=100, 1.000 y 10.000:",
          [contar_pares(n) for n in (100, 1_000, 10_000)])

    print("\nEJERCICIO 4 — Triangulación")
    print("Para n=5:", triangulos_y_diagonales(5))

    print("\nEJERCICIO 5 — Comparación de crecimiento")
    for n in (10, 100, 1_000):
        print(f"n={n}: modelo A/B = {comparar_crecimiento(n)}")
