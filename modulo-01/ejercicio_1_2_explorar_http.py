"""
Ejercicio 1.2 · Explorar HTTP con Python

Usaremos https://httpbin.org, un servicio de pruebas que te "refleja" lo que
le envías. Así puedes VER los encabezados y códigos que estudiaste.

Si httpbin no responde (a veces se satura), cambia BASE_URL por
"https://postman-echo.com". Ojo: ahí los nombres de los encabezados llegan
en minúsculas ("content-type" en lugar de "Content-Type").

Busca las marcas TODO (lo que debes programar) y PREGUNTA (lo que debes
responder en un comentario dentro de este mismo archivo).
"""
import requests

BASE_URL = "https://httpbin.org"
TIMEOUT = 10  # segundos; nunca hagas peticiones sin límite de tiempo


def parte_a_get_con_accept():
    """GET a /headers enviando Accept. El servidor te devuelve lo que recibió."""
    print("\n=== Parte A · GET con Accept ===")
    respuesta = requests.get(
        f"{BASE_URL}/headers",
        headers={"Accept": "application/json"},
        timeout=TIMEOUT,
    )
    print("Código de estado:", respuesta.status_code)
    print("Content-Type de la respuesta:", respuesta.headers.get("Content-Type"))
    print("Encabezados que recibió el servidor:")
    for nombre, valor in respuesta.json()["headers"].items():
        print(f"  {nombre}: {valor}")

    # PREGUNTA A1: ¿Aparece tu Accept entre los encabezados que recibió el servidor?
    # Respuesta:
    # PREGUNTA A2: ¿Quién puso el Content-Type de la respuesta: tú o el servidor? ¿Por qué?
    # Respuesta:


def parte_b_post_con_json():
    """POST a /post enviando una decisión sobre una diferencia."""
    print("\n=== Parte B · POST con cuerpo JSON ===")
    decision = {"diferencia_id": 7, "decision": "ajustar"}

    # TODO B1: haz un requests.post a f"{BASE_URL}/post" usando json=decision
    #          y timeout=TIMEOUT. Guarda el resultado en la variable `respuesta`.
    # TODO B2: imprime el código de estado.
    # TODO B3: imprime el Content-Type que RECIBIÓ el servidor:
    #          respuesta.json()["headers"]["Content-Type"]
    # TODO B4: imprime lo que el servidor entendió de tu cuerpo:
    #          respuesta.json()["json"]

    # PREGUNTA B1: tú no escribiste ningún Content-Type. ¿Quién lo puso y por qué?
    # Respuesta:
    # PREGUNTA B2: en una API real que crea un recurso, ¿qué código esperarías en lugar de 200?
    # Respuesta:


def interpretar_codigo(codigo: int) -> str:
    """Traduce un código HTTP a un mensaje claro para el analista del portal."""
    # TODO C1: devuelve un mensaje distinto para 200, 201, 400, 401, 403, 404 y 500,
    #          y uno genérico para cualquier otro código.
    #          Ejemplo para 403: "Tu usuario no tiene permiso para esta acción."
    #          Pista: usa if/elif o un diccionario con .get()
    return "TODO: sin interpretar"


def parte_c_codigos():
    """httpbin responde con el código que le pidas en /status/<código>."""
    print("\n=== Parte C · Interpretar códigos de estado ===")
    for codigo in [200, 201, 400, 401, 403, 404, 500]:
        respuesta = requests.get(f"{BASE_URL}/status/{codigo}", timeout=TIMEOUT)
        print(f"{respuesta.status_code} -> {interpretar_codigo(respuesta.status_code)}")

    # PREGUNTA C1: requests NO lanzó error con 404 ni con 500. ¿Por qué eso es
    #              peligroso si un programa solo revisa si "hubo respuesta"?
    # Respuesta:


if __name__ == "__main__":
    parte_a_get_con_accept()
    parte_b_post_con_json()
    parte_c_codigos()
