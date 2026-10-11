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
    # Respuesta: Si aparece, en la parte A aparece el Accpet: aplication/json que es el json con el cual me estari respondiendi
    # PREGUNTA A2: ¿Quién puso el Content-Type de la respuesta: tú o el servidor? ¿Por qué?
    # Respuesta: Yo nunca lo puse y efectivamente esa els la pregunt, me parece fue el serviudoer,,ya que es ka etiquetapegada que describe el cuerpo que viaja


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
    respuesta = requests.post(f"{BASE_URL}/post", json=decision, timeout=TIMEOUT)
    print("Código de estado:", respuesta.status_code)
    print("Contente-Type que recibió el servidor:", respuesta.json()["headers"]["Content-Type"])
    print("Lo que entendió el servidor:", respuesta.json()["json"])

    # PREGUNTA B1: tú no escribiste ningún Content-Type. ¿Quién lo puso y por qué?
    # Respuesta: Lo puso el servidor, porque de esta es la manera en la cual sabemos que es lo que trae en la caja
    # PREGUNTA B2: en una API real que crea un recurso, ¿qué código esperarías en lugar de 200?
    # Respuesta: Me gustaria tener un 401 ya que yo aún no le he dado los permisos para ingresar 


def interpretar_codigo(codigo: int) -> str:
    """Traduce un código HTTP a un mensaje claro para el analista del portal."""
    # TODO C1: devuelve un mensaje distinto para 200, 201, 400, 401, 403, 404 y 500,
    #          y uno genérico para cualquier otro código.
    #          Ejemplo para 403: "Tu usuario no tiene permiso para esta acción."
    #          Pista: usa if/elif o un diccionario con .get()

    mensajes = {
        200: "Consulta atendida correctamente.",
        201: "Registro creado correctamente.",
        400: "La solicitud tiene datos inválidos; revisa lo que capturaste.",
        401: "Tu sesión no es válida o venció; inicia sesión de nuevo.",
        403: "Tu usuario no tiene permiso para esta acción.",
        404: "El lote o registro solicitado no existe.",
        500: "Error interno del servidor; avisa a soporte.",
    }
    return mensajes.get(codigo, f"Código {codigo} no contemplado; avisa a soporte.")


def parte_c_codigos():
    """httpbin responde con el código que le pidas en /status/<código>."""
    print("\n=== Parte C · Interpretar códigos de estado ===")
    for codigo in [200, 201, 400, 401, 403, 404, 500]:
        respuesta = requests.get(f"{BASE_URL}/status/{codigo}", timeout=TIMEOUT)
        print(f"{respuesta.status_code} -> {interpretar_codigo(respuesta.status_code)}")

    # PREGUNTA C1: requests NO lanzó error con 404 ni con 500. ¿Por qué eso es
    #              peligroso si un programa solo revisa si "hubo respuesta"?
    # Respuesta: Esto es debiod a que si mi programa solo ve si hay una respuesta, podria tomar el json devuelto como una respuesta valida , esto significara mostrarle 
    # al analista data erronea o que esta corrupta


if __name__ == "__main__":
    parte_a_get_con_accept()
    parte_b_post_con_json()
    parte_c_codigos()
