def calcular_puntaje(stats_equipo):
    """
    Calcula el puntaje de un equipo en una ronda en particular.
    La fórmula es: +3 por innovación, +1 por presentación, -1 si hay errores graves.
    """
    puntos = (stats_equipo['innovacion'] * 3) + (stats_equipo['presentacion'] * 1)
    if stats_equipo['errores']:
        puntos -= 1
    return puntos

def imprimir_tabla(estadisticas):
    """
    Muestra una tabla con las estadísticas acumuladas de todos los equipos,
    ordenada por puntaje total de forma descendente.
    """
    # Encabezado de la tabla
    print(f"{'Equipo':<10} | {'Innovación':<10} | {'Presentación':<12} | {'Errores':<8} | {'MER':<5} | {'Puntos Total':<12}")
    print("-" * 75)

    # Ordenar los equipos por el puntaje total acumulado
    equipos_ordenados = sorted(estadisticas.items(), key=lambda item: item[1]['puntos_total'], reverse=True)

    # Imprimir la fila de cada equipo
    for nombre, stats in equipos_ordenados:
        print(f"{nombre:<10} | {stats['innovacion']:<10} | {stats['presentacion']:<12} | {stats['errores']:<8} | {stats['mejores']:<5} | {stats['puntos_total']:<12}")