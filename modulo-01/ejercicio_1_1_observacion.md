# Ejercicio 1.1 · Observar una petición real

Sitio observado: https://developer.mozilla.org, con Chrome DevTools (pestaña Network, filtro Doc).

## Observación 1 · Respuesta completa (caché desactivada)

- **URL:** https://developer.mozilla.org/es/
- **Método:** GET
- **Código de estado:** 200 OK
- **Content-Type de la respuesta:** text/html
- **Qué contiene la respuesta:** Un documento HTML que empieza con <!doctype html>, en español (lang="es"), con el título "MDN Web Docs" y código JavaScript dentro de etiquetas <script>.
- **Duración aproximada:** [ESCRIBE AQUÍ EL TIEMPO]
- **Tamaño transferido:** [ESCRIBE AQUÍ LOS kB]
- **Qué hizo el navegador con ese contenido:** Interpretó el HTML y, a partir de él, hizo muchas peticiones más (unas 75 en total) para pedir estilos (CSS), código JavaScript, fuentes e imágenes. Con todo eso dibujó la página en la pantalla.

## Observación 2 · Respuesta desde caché

- **URL:** https://developer.mozilla.org/es/
- **Método:** GET
- **Código de estado:** 304 Not Modified
- **Content-Type de la respuesta:** No aparece, porque el servidor no mandó una página nueva, solo la confirmación de que mi copia guardada seguía vigente. Sin cuerpo, no hay contenido que etiquetar.
- **Qué contiene la respuesta:** DevTools muestra el mismo HTML, pero es la copia que el navegador ya tenía guardada, no una nueva enviada por el servidor.
- **Duración aproximada:** [ESCRIBE AQUÍ EL TIEMPO]
- **Tamaño transferido:** 0.2 kB
- **Qué hizo el navegador con ese contenido:** Usó la copia que tenía guardada en caché y la mostró sin volver a descargarla.

## Hallazgos adicionales

- **IP y puerto del servidor (Remote Address):** [2a04:4e42:2e::347]:443. Es una dirección IPv6 y el puerto 443 de HTTPS.
- **Etag (huella de la versión):** "5305bb283e84c21325a325908f262256"
- **If-None-Match (lo que preguntó el navegador):** "5305bb283e84c21325a325908f262256". Es idéntico al Etag, por eso el servidor respondió 304.
- **Quién respondió (X-Served-By):** cache-lax-kwhp1940099-LAX. La respuesta vino de un servidor de caché en Los Ángeles (LAX es el código de su aeropuerto), no del servidor principal de MDN. Esa red de servidores repartidos por el mundo se llama CDN y sirve para responder más rápido desde un punto cercano al usuario.
- **Accept-Language:** es-ES. Mi navegador indicó que prefiero español, así que MDN me dirigió a la versión /es/ y el HTML llegó con lang="es".

## Reflexión

1. ¿Qué cambió entre la observación 1 y la 2, y por qué?

   En la observación 1 desactivé la caché, así que el navegador pidió la página sin mostrar la huella de su copia. El servidor respondió 200 OK y mandó el HTML completo. En la observación 2 el navegador envió If-None-Match con el Etag de su copia guardada; como coincidía con la versión actual, el servidor respondió 304 Not Modified sin mandar la página, y solo viajaron 0.2 kB. Resultado: menos datos y una carga más rápida.

2. ¿En qué se parece y en qué se diferencia esta respuesta de la que devolvería
   la API del portal al consultar el lote 42?

   Se parecen en que ambas son peticiones GET por HTTPS y sus respuestas tienen código de estado, encabezados y cuerpo. Se diferencian en el contenido y en quién lo lee: MDN devuelve HTML (text/html) para que el navegador dibuje una página que ve una persona. La API del lote 42 devolvería JSON (application/json), por ejemplo {"lote_id": 42, "estado": "pendiente", "diferencias": 3}, para que un programa lo procese y lo convierta en una tabla. Además, la API tendría que validar autenticación y permisos antes de responder, y un 200 no garantizaría que la cifra de diferencias esté bien calculada.