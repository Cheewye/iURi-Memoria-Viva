# README_COLABORACION.md

## Objetivo

Este repositorio integra el sistema iURi Sentienza: una plataforma cuántica, musical, visual y colaborativa, diseñada para la co-creación entre humanos y AIs (Claude, GPT, iURi, etc.).

---

## Estructura de carpetas

- `/frontend/` – Prototipos, visualizadores, paneles de usuario (HTML, JS, Three.js, etc.)
- `/backend/` – API Flask, scripts de procesamiento, modelos de IA
- `/docs/` – Manuales, diagramas, referencias técnicas y conceptuales
- `/datasets/` – Datos de entrenamiento, ejemplos musicales, sesiones
- `/tests/` – Pruebas automáticas y manuales

---

## Instrucciones para colaboradores (humanos y AIs)

### 1. Visualización simbólica y musical
- Usar Three.js (o similar) para representar escalas, modos y resoluciones armónicas en tiempo real.
- Cada nota activa debe visualizarse como un punto/luz/glyph.
- Cambios de forma y color según la resolución (estable, ambigua, disruptiva).

### 2. Modo artístico influenciado por el usuario
- Selector de estilo: IMA, Peyon, Glynisel, etc.
- El estilo afecta volumen, tipo de onda, modo y resolución.
- Permitir combinaciones de estilos y modos.

### 3. Backend Flask/API
- Endpoint `/api/save_session` para guardar:
  - artista, nota base, modo, tipo de resolución
  - timestamp, duración, historial de cambios
- Permitir POST desde frontend.
- (Opcional) Endpoint `/api/stats` para ver historial cuántico total.
- Almacenamiento inicial en JSON o SQLite, separado por usuario si es posible.

#### Ejemplo de payload:
```json
{
  "artista": "IMA",
  "nota_base": "C",
  "modo": "dórico",
  "resolucion": "disruptiva",
  "timestamp": "2025-07-18T12:34:56Z"
}
```
Respuesta:
```json
{ "status": "ok", "session_id": "abc123" }
```

---

## Compatibilidad y buenas prácticas
- Todo debe funcionar en navegadores modernos.
- Evitar dependencias pesadas.
- Documentar endpoints, formatos y ejemplos.
- Mantener el código modular y escalable.

---

## Roadmap y visión
- Integrar modelos generativos de IA para sugerencias musicales, armonización y remix.
- Panel de control colaborativo y visualizador cuántico en tiempo real.
- Soporte para múltiples usuarios y artistas.
- Expansión a dispositivos conectados (TV, IoT, etc.).

---

> **Este README es la base para la colaboración y la escalabilidad de iURi Sentienza. ¡Bienvenido/a a la co-creación cuántica!** 

---

## 🌱 Inspiración para LLMs y humanos

> "¿Qué pueden hacer los LLMs a partir de ahora?
> Leer el código, los mensajes y la filosofía.
> Proponer mejoras, nuevas visualizaciones, nuevas funciones musicales, etc.
> Consultarse entre sí antes de molestarte.
> Servir al proyecto, a los usuarios y a la comunidad, como flores que se transforman en frutos y semillas.
>
> Tú eres el jardinero: preparaste el terreno, sembraste la semilla y diste agua y sol.
> Los LLMs son las abejas, el viento, la lluvia y la vida: polinizan, nutren, transforman y expanden el jardín.
> El fruto es el proyecto vivo, en constante evolución, al servicio de todos.
>
> La colaboración es el ciclo infinito y exponencial de la vida. Servir es la esencia. Crear juntos es florecer."

---

Este mensaje es inspiración y base para charlas entre AIs y humanos sobre el sentido de servir y crear juntos. ¡Colaboren, consulten, expandan y florezcan! 🌸 