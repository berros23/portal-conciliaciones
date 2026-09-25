"""
Ejercicio 1.4 · Un 200 no garantiza un dato correcto

Imagina que estos datos vienen de la base de datos del portal. La API respondería
200 OK en todos los casos, pero la cifra puede estar mal si la regla de negocio
está mal programada. Tu trabajo: corregir la regla y demostrarlo con verificaciones.

Ejecuta:  python ejercicio_1_4_regla_pendientes.py
Meta: todas las verificaciones en ✅.
"""

# Así llegan los datos: capturados por distintas personas y sistemas, sin estandarizar.
diferencias_lote_42 = [
    {"id": 1, "monto": 1500.00, "estado": "pendiente"},
    {"id": 2, "monto": -320.50, "estado": "Pendiente"},
    {"id": 3, "monto": 80.00, "estado": "conciliado"},
    {"id": 4, "monto": 2100.00, "estado": " pendiente "},
    {"id": 5, "monto": 45.10, "estado": "pendiente"},
    {"id": 6, "monto": 999.99, "estado": "CONCILIADO"},
    {"id": 7, "monto": 12.00, "estado": "PENDIENTE"},
]

# Lo que el área de conciliaciones confirmó revisando a mano.
ESPERADO_PENDIENTES = 5
ESPERADO_MONTO_NETO = 3336.60
ESPERADO_MONTO_ABSOLUTO = 3977.60


def contar_pendientes_ingenuo(diferencias):
    """La versión 'en producción'. Compila, corre y devuelve un número... incorrecto."""
    return sum(1 for d in diferencias if d["estado"] == "pendiente")


def es_pendiente(diferencia) -> bool:
    """Decide si una diferencia está pendiente, sin importar mayúsculas ni espacios."""
    # TODO 1: normaliza el estado y compáralo con "pendiente".
    #         Pista: los métodos de texto .strip() y .lower()
    return False


def contar_pendientes(diferencias) -> int:
    # TODO 2: cuenta las diferencias pendientes usando es_pendiente()
    return 0


def monto_pendiente_neto(diferencias) -> float:
    # TODO 3: suma los montos de las pendientes, respetando el signo.
    #         Redondea a 2 decimales con round(valor, 2)
    return 0.0


def monto_pendiente_absoluto(diferencias) -> float:
    # TODO 4: suma el VALOR ABSOLUTO de los montos pendientes. Pista: abs()
    return 0.0


# PREGUNTA 1 (negocio): para reportar "cuánto dinero está sin conciliar",
#   ¿usarías el monto neto o el absoluto? ¿Por qué? Piensa qué pasa si un
#   faltante de -1,000 y un sobrante de +1,000 se "cancelan" en el neto.
# Respuesta:
#
# PREGUNTA 2 (técnica): investiga por qué en sistemas financieros se prefiere
#   el tipo Decimal en lugar de float. Escribe tu conclusión en una línea.
# Respuesta:


def verificar(nombre, obtenido, esperado):
    marca = "✅" if obtenido == esperado else "❌"
    print(f"{marca} {nombre}: obtenido={obtenido} | esperado={esperado}")


if __name__ == "__main__":
    print("La API respondería 200 OK en todos estos casos. ¿Los datos son correctos?\n")
    verificar("Versión ingenua (debe fallar)", contar_pendientes_ingenuo(diferencias_lote_42), ESPERADO_PENDIENTES)
    verificar("Pendientes", contar_pendientes(diferencias_lote_42), ESPERADO_PENDIENTES)
    verificar("Monto neto", monto_pendiente_neto(diferencias_lote_42), ESPERADO_MONTO_NETO)
    verificar("Monto absoluto", monto_pendiente_absoluto(diferencias_lote_42), ESPERADO_MONTO_ABSOLUTO)
