# Ejercicio 1.3 · Contrato de la API del portal

Eres quien diseña la API. Todavía no hay código: solo el **contrato**, es decir,
qué se puede pedir, cómo y qué se responde. Esto es trabajo de arquitectura real.

## Reglas del portal

- Solo usuarios con sesión válida pueden usar la API.
- Un analista solo ve los lotes de su área.
- Solo un supervisor puede aprobar decisiones de ajuste.

## Contrato

La primera fila está resuelta como modelo. Completa las demás.

| # | Acción | Método | Ruta | ¿Lleva cuerpo? ¿Qué trae? | Código de éxito | Errores posibles y cuándo ocurren |
|---|---|---|---|---|---|---|
| 1 | Consultar un lote por su id | GET | `/api/lotes/{lote_id}` | No | 200 | 401 sin sesión · 403 lote de otra área · 404 lote inexistente |
| 2 | Dar de alta un lote nuevo | POST |`/api/lotes` | Si, datos del lote com o su referencia y área |201 | 401 sin sesión · 403 lote de otra área · 409 Existe una duplicidad del lote|
| 3 | Listar las diferencias de un lote |GET | `/api/lotes/{lote_id}/diferencias`| No| 200 | 401 sin sesión · 403 lote de otra área · 404 lote inexistente|
| 4 | Cambiar solo el estado de una diferencia | PATCH | `/api/diferencias/{diferencia_id}`| Si, el estado en que se encuentra el patch | 200 |401 sin sesión · 403 diferencia de otra área · 404 diferencia inexistente · 400 estado inválido · 409 transición de estado no permitida | |
| 5 | Registrar una decisión sobre una diferencia |POST | `/api/diferencias/{diferencia_id}/decisiones` | Si, el tipo de decisión justificada y la correción al modelo de ajust |201 | 401 sin sesión · 403 diferencia de otra área · 404 diferencia inexistente · 400 estado inválido · 409 decisión incompatible|
| 6 | Eliminar una nota capturada por error | DELETE|`/api/notas/{nota_id}`| No | 204 | 401 sin sesión · 403 sin permiso sobre la nota o lote de otra área · 404 nota inexistente|

## Preguntas de diseño

1. En la acción 5, ¿qué cuerpo JSON enviarías? Escribe un ejemplo. 

{
  "tipo": "ajuste",
  "justificacion": "Se detectó un cargo duplicado",
  "monto_ajuste": -150.00
}

2. Si un analista (no supervisor) intenta registrar una decisión de ajuste, ¿qué códigoresponde la API y por qué no es 401? 

Tendría que arrojar el 403 Forbidden, esto debiod a que se sabe quine es pero no tiene permisos de ajuste, solo los supervisores tienen ese permiso

3. En la acción 4, ¿por qué PATCH y no PUT? 

Porque solo estamos generando un ajuste puntual a un solo registro, por eso PATCH, en el caso de PUT estariamos cambiando todo el renglon
