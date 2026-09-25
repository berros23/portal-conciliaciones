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
| 2 | Dar de alta un lote nuevo | | | | | |
| 3 | Listar las diferencias de un lote | | | | | |
| 4 | Cambiar solo el estado de una diferencia | | | | | |
| 5 | Registrar una decisión sobre una diferencia | | | | | |
| 6 | Eliminar una nota capturada por error | | | | | |

## Preguntas de diseño

1. En la acción 5, ¿qué cuerpo JSON enviarías? Escribe un ejemplo.
2. Si un analista (no supervisor) intenta registrar una decisión de ajuste, ¿qué código
   responde la API y por qué no es 401?
3. En la acción 4, ¿por qué PATCH y no PUT?
